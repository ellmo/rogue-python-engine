import tile
import thing

from locals import *
from errors import *
from file_ops import *

class RpeMap(object):
    def __init__(self, map_path):
        parsed_map = parse_to_lists(map_path)
        self._tiles = []
        self._things = []
        self._start_position = None
        for y, row in zip(range(len(parsed_map)), parsed_map):
            _tile_row = []
            for x, column in enumerate(row):
                _tile_to_append = tile.create_based_on_char(column)
                _tile_to_append.x = x
                _tile_to_append.y = y
                if column is 's':
                    if self._start_position is None:
                        self._start_position = (x, y)
                    else:
                        raise MultiplePlayerStartError()
                elif column is 'b':
                    _tile_to_append.things.append(thing.Thing())
                    self._things.append(_tile_to_append)
                _tile_row.append(_tile_to_append)
            self._tiles.append(_tile_row)
        if self._start_position is None:
            raise NoPlayerStartError()

    @property
    def tiles(self):
        return self._tiles

    @property
    def things(self):
        return self._things

    @property
    def start_position(self):
        return self._start_position

