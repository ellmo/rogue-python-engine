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
        self._map.things

    def __cast_background(self):
        self._surface.blit(self._background, (0, 0))

    def __cast_rays(self):
        # based on http://lodev.org/cgtutor/raycasting.html
        for x_column in range(self._width):
            # initiate a Ray Object
            ray_obj = ray.Ray(self, x_column)
            ray_obj.render_texture()
            self._zbuffer.append(ray_obj.wall_distance)

    def __compare_thing_distance(thing1, thing2):
        thing1_dist = math.sqrt((thing1[0] -self._camera.x) ** 2 + (thing1[1] -self._camera.y) ** 2)
        thing2_dist = math.sqrt((s2[0] -self._camera.x) ** 2 + (thing2[1] -self._camera.y) ** 2)
        if thing1_dist > thing2_dist:
            return -1
        elif thing1_dist == thing2_dist:
            return 0
        else:
            return 1
