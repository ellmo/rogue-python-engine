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
        # Clearing the buffer after each render is paramount!
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
            # Save the distance to the drawn wall in the buffer. This lets you quickly test,
            # wether the Thing's sprite you're trying to render isn't in fact behind a wall.
            self.zbuffer.append(ray_obj.wall_distance)

    def __cast_things(self):
        # based on http://lodev.org/cgtutor/raycasting3.html

        # Sort all things by distance from current camera position.
        sorted_things = sorted(self._map.things, key=self.tile_distance)
        # Draw things starting from the farthermost to the closest (hence the reversal).
        for tile in reversed(sorted_things):
            # Position of the Thing, relative to camera's current position
            # the 0.5 * something part servers to push the Thing half a tile back.
            sprite_x = tile.x - self.camera.x + (0.5 * self.camera.dirx)
            sprite_y = tile.y - self.camera.y + (0.5 * self.camera.diry)
            # Creating the transformation matrix.
            inv_det = 1.0 / (self.camera.planex * self.camera.diry - self.camera.dirx * self.camera.planey)
            transform_x = inv_det * (self.camera.diry * sprite_x - self.camera.dirx * sprite_y)
            transform_y = inv_det * (self.camera.planex * sprite_y - self.camera.planey * sprite_x)
            if transform_y < 0:
                continue # the object is not even in front of the camera, go to next one
            else:
                # Calculate where on the screen to start drawing the sprite and where to end.
                sprite_surface_x = int((self.width / 2) * (1 + transform_x / transform_y))
                sprite_height = abs(int(self.height / (transform_y)))
                sprite_width = abs(int(self.height / (transform_y)))
                draw_start_y = -sprite_height / 2 + self.height / 2
                draw_end_y = sprite_height / 2 + self.height / 2
                draw_start_x = -sprite_width / 2 + sprite_surface_x
                draw_end_x = sprite_width / 2 + sprite_surface_x
                if sprite_height < 1000:
                    for stripe in range(draw_start_x, draw_end_x):
                        if (
                            stripe >= 0 and stripe < self.width and # is the stripe even within screen boundaries?
                            transform_y < self.zbuffer[stripe] # isn't this stripe obscured by a wall?
                        ):
                            # Find out which column of pixels to grab from the pixel-table turned image.
                            tex_x = int((stripe - (-sprite_width / 2 + sprite_surface_x))
                                * 64 / sprite_width)
                            # Finally blit a column of pixels.
                            self.surface.blit(
                                pygame.transform.scale(
                                    tile.thing.sprite.converted[tex_x],
                                    (1, sprite_height)
                                ),
                                (stripe, draw_start_y))

    def __clear_buffer(self):
        # Clears the 'depth' buffer after all walls and sprites were drawn.
        # Prepares new buffer for a new render.
        self._zbuffer = []