import pdb
import pygame

import camera
import map

class Renderer(object):
  def __init__(self, surface, map):
    self._surface = surface
    # self._camera = camera.Camera(self)
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

  def render(self):
    self._surface.blit(self._background, (0, 0))