import pygame
import math

import ray
from ..locals import *

class Renderer(object):
    def __init__(self, surface, rpe_map, camera):
        self._camera = camera
        self._surface = surface
        self._map = rpe_map
        self._width = self._surface.get_width()
        self._height = self._surface.get_height()
        self._background = pygame.transform.scale(
            pygame.image.load("res/bkg.png").convert(),
            (self._width, self._height)
        )
        self._zbuffer = [] # for sorting sprite distance

    @property
    def surface(self):
        return self._surface

    @property
    def camera(self):
        return self._camera

    @property
    def rpe_map(self):
        return self._map

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @property
    def zbuffer(self):
        return self._zbuffer
    @zbuffer.setter
    def zbuffer(self, value):
        self._zbuffer = value

    def render(self):
        self.__cast_background()
        self.__cast_rays()
        self.__cast_things()
        self.__clear_buffer()

    def tile_distance(self, tile):
        return math.sqrt((tile.x -self._camera.x) ** 2 + (tile.y -self._camera.y) ** 2)

    def __cast_background(self):
        self._surface.blit(self._background, (0, 0))

    def __cast_rays(self):
        # based on http://lodev.org/cgtutor/raycasting.html
        for x_column in range(self._width):
            # initiate a Ray Object
            ray_obj = ray.Ray(self, x_column)
            ray_obj.render_texture()
            self.zbuffer.append(ray_obj.wall_distance)

    def __cast_things(self):
        sorted_things = sorted(self._map.things, key=self.tile_distance)
        for tile in sorted_things:
            sprite_x = tile.x - self.camera.x + (0.5 * self.camera.dirx)
            sprite_y = tile.y - self.camera.y + (0.5 * self.camera.diry)
            # creating
            inv_det = 1.0 / (self.camera.planex * self.camera.diry - self.camera.dirx * self.camera.planey)
            transform_x = inv_det * (self.camera.diry * sprite_x - self.camera.dirx * sprite_y)
            transform_y = inv_det * (self.camera.planex * sprite_y - self.camera.planey * sprite_x)
            if (transform_y == 0):
                transform_y = 0.0000001
            sprite_surface_x = int((self.width / 2) * (1 + transform_x / transform_y))
            sprite_height = abs(int(self.height / (transform_y)))
            draw_start_y = -sprite_height / 2 + self.height / 2
            draw_end_y = sprite_height / 2 + self.height / 2
            #calculate width of the sprite
            sprite_width = abs(int(self.height / (transform_y)))
            draw_start_x = -sprite_width / 2 + sprite_surface_x
            draw_end_x = sprite_width / 2 + sprite_surface_x
            if sprite_height < 1000:
                for stripe in range(draw_start_x, draw_end_x):
                    tex_x = int(256 * (stripe - (-sprite_width / 2 + sprite_surface_x)) * 64 / sprite_width) / 256
                    if (
                        transform_y > 0 and
                        stripe >= 0 and
                        stripe < self.width and
                        transform_y < self.zbuffer[stripe]
                    ):
                        self.surface.blit(pygame.transform.scale(tile.thing.sprite.converted[tex_x], (1, sprite_height)), (stripe, draw_start_y))

    def __clear_buffer(self):
        self._zbuffer = []