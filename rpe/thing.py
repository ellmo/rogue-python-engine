import sprite

class Thing(object):
    def __init__(self, name='barrel', blocking=True, sprite=sprite.Sprite()):
        self._name = name
        self._blocking = blocking
        self._sprite = sprite

    @property
    def name(self):
        return self._name

    @property
    def blocking(self):
        return self._blocking

    @property
    def sprite(self):
        return self._sprite