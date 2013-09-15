import pdb
import pygame

from locals import *

class Texture(object):
  def __init__(self, image_path='res/purp.png'):
    self._image_path = image_path
    self._image = pygame.image.load(image_path)

  @property
  def image(self):
    return self._image

  @property
  def image_path(self):
    return self._image_path




  def convert(self):
    self._image.convert()
