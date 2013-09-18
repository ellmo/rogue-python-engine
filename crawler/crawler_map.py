import tile

from locals import *
from errors import *

class CrawlerMap(object):
  def __init__(self):
    self._tiles = []
    self._items = []
    self._start_position = None
    for row in MAP_01:
      _tile_row = []
      for column in row:
        if column is 5:
          if self._start_position is None:
            self._start_position = (row.index(column), MAP_01.index(row))
          else:
            raise MultiplePlayerStartError()
        _tile_to_append = tile.create_based_on_number(column)
        _tile_row.append(_tile_to_append)
      self._tiles.append(_tile_row)
    if self._start_position is None:
      raise NoPlayerStartError()

  @property
  def tiles(self):
    return self._tiles

  @property
  def start_position(self):
      return self._start_position

