import texture

from locals import *

class Tile(object):
    def __init__(self, solid=False, seethru=True, texture=None):
        self._solid = solid
        self._texture = texture
        self._things = []

    @property
    def solid(self):
        return self._solid
    @solid.setter
    def solid(self, value):
        self._solid = value

    @property
    def seethru(self):
        return self._seethru
    @seethru.setter
    def seethru(self, value):
        self._seethru = value

    @property
    def texture(self):
        return self._texture
    @texture.setter
    def texture(self, value):
        self._texture = value

    @property
    def things(self):
            return self._things
    @things.setter
    def things(self, value):
            self._things = value

def create_based_on_char(char):
    if char == '1':
        return Tile(True, False, texture.Texture())
    elif char == '2':
        return Tile(True, False, texture.Texture('res/colorstone.png'))
    elif char == '3':
        return Tile(True, False, texture.Texture('res/wood.png'))
    else:
        return Tile()
