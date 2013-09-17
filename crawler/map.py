import pdb
import tile

from locals import *
from errors import *

class Map(object):
  def __init__(self):
    self._tiles = []
    self._items = []
    self._start_position = None
    for row in MAP_01:
      _tile_row = []
      for column in row:
        if column is 5:
          if self._start_position is None:
            self._start_position = (MAP_01.index(row), row.index(column))
          else:
            raise MultiplePlayerStartError('Loaded map has multiple player starts.')
        _tile_to_append = tile.create_based_on_number(column)
        _tile_row.append(_tile_to_append)
      self._tiles.append(_tile_row)
    if self._start_position is None:
      raise NoPlayerStartError('Loaded map has no player start.')

  @property
  def tiles(self):
    return self._tiles

  @property
  def start_position(self):
      return self._start_position

