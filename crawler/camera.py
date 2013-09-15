import pdb
import pygame

import renderer

class Camera(object):
  def __init__(self, renderer):
    self._renderer = renderer
    self._surface = renderer.surface
    self._width = self._surface.get_width()
    self._height = self._surface.get_height()
    self._background = pygame.transform.scale(
      pygame.image.load("res/bkg.png").convert(),
      (self._width, self._height)
    )

  def draw(self):
    self._surface.blit(self._background, (0, 0))
