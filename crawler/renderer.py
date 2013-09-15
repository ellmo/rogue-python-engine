import pdb
import pygame

import camera
import map

class Renderer(object):
  def __init__(self, surface, map):
    self._surface = surface
    self._camera = camera.Camera(self)

  @property
  def surface(self):
      return self._surface

  @property
  def camera(self):
      return self._camera

  def render(self):
    self._camera.draw()