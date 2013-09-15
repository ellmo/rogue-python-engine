import pdb
import tile

from locals import *

class Map(object):
  def __init__(self):
    self._tiles = []
    for row in MAP_01:
      _tile_row = []
      for column in row:
        _tile_to_append = tile.create_based_on_number(column)
        _tile_row.append(_tile_to_append)
      self._tiles.append(_tile_row)

  @property
  def tiles(self):
    return self._tiles
  @tiles.setter
  def tiles(self, value):
    self._tiles = value

