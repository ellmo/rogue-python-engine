import pygame

from locals import *

class Texture(object):
  def __init__(self, image_path='res/purp.png'):
    self._image_path = image_path
    self._image = pygame.image.load(image_path)
    self._converted = None
    self._converted_darkened = None

  @property
  def image(self):
    return self._image

  @property
  def image_path(self):
    return self._image_path

  @property
  def converted(self):
    if self._converted is None:
      self._converted = self.__convert_to_pixel_table()
      self._converted_darkened = self.__convert_to_pixel_table(True)
    return self._converted

  @property
  def converted_darkened(self):
    if self._converted is None:
      self._converted = self.__convert_to_pixel_table()
      self._converted_darkened = self.__convert_to_pixel_table(True)
    return self._converted_darkened

  def __convert_to_pixel_table(self, darken=False):
    image = self._image
    table = []
    if darken:
      image.set_alpha(192)
    for i in range(image.get_width()):
      s = pygame.Surface((1, image.get_height())).convert()
      s.blit(image, (-i, 0))
      table.append(s)
    return table