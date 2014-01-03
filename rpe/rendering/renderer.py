import pygame
import math

import ray

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
            self._zbuffer.append(ray_obj.wall_distance)

    def __cast_things(self):
        sorted_things = sorted(self._map.things, key=self.tile_distance)
