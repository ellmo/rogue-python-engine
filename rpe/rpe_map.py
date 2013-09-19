import tile

from locals import *
from errors import *
from file_ops import *

class RpeMap(object):
  def __init__(self, map_path):
    parsed_map = parse_to_lists(map_path)
    self._tiles = []
    self._start_position = None
    for row in parsed_map:
      _tile_row = []
      for column in row:
        if column is 's':
          if self._start_position is None:
            self._start_position = (row.index(column), parsed_map.index(row))
          else:
            raise MultiplePlayerStartError()
        _tile_to_append = tile.create_based_on_char(column)
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

