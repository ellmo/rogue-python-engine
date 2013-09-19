import pygame
import math

import camera
import rpe_map
import ray

from locals import *
from time import sleep

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

  def render(self):
    self._surface.blit(self._background, (0, 0))

  def raycast(self):
    # based on http://lodev.org/cgtutor/raycasting.html
    for x_column in range(self._width):
      #calculate ray position and direction
      camera_x = float(2 * x_column / float(self._width) - 1) #x-coordinate in camera space
      ray_dirx = self._camera.dirx + self._camera.planex * camera_x
      ray_diry = self._camera.diry + self._camera.planey * camera_x
      if ray_dirx == 0: ray_dirx = 0.00001
      if ray_diry == 0: ray_diry = 0.00001
      mapx = int(self._camera.x)
      mapy = int(self._camera.y)
      # initiate a Ray Object
      ray_obj = ray.Ray(self, ray_dirx, ray_diry)

      #x coordinate on the texture
      tex_x = int(ray_obj.wall_x * float(TEX_SIZE))
      if(ray_obj.side == 0 and ray_dirx > 0):
        tex_x = TEX_SIZE - tex_x - 1;
      if(ray_obj.side == 1 and ray_diry < 0):
        tex_x = TEX_SIZE - tex_x - 1;

      if ray_obj.line_height > 1000:
        ray_obj.line_height = 1000
        ray_obj.draw_start = -1000 /2 + self._height/2
      if not ray_obj.tile.texture is None:
        img = ray_obj.tile.texture.converted if ray_obj.side == 0 else ray_obj.tile.texture.converted_darkened
        self._surface.blit(pygame.transform.scale(img[tex_x], (1, ray_obj.line_height)), (x_column, ray_obj.draw_start))