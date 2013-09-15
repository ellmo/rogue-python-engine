import pdb
import pygame

from locals import *

class Texture(object):
  def __init__(self, image_path='res/purp.png'):
    self._image = pygame.image.load(image_path)

  @property
  def image(self):
    return self._image
  @image.setter
  def image(self, value):
    self._image = value

  def convert(self):
    self._image.convert()
