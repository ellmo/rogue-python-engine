import pdb
import texture

from locals import *

class Tile(object):
  def __init__(self, solid=False, walkthru=True, texture=None):
    self._walkthru = walkthru
    self._solid = solid
    self._texture = texture

  @property
  def solid(self):
    return self._solid
  @solid.setter
  def solid(self, value):
    self._solid = value

  @property
  def walkthru(self):
    return self._walkthru
  @walkthru.setter
  def walkthru(self, value):
    self._walkthru = value

  @property
  def texture(self):
    return self._texture
  @texture.setter
  def texture(self, value):
    self._texture = value

def create_based_on_number(number):
  if number == 0 or number == 5:
    return Tile()
  else:
    return Tile(True, False, texture.Texture())
