import math

class Camera(object):
  def __init__(self, position, direction_vector):
    self._x = int(position[0])
    self._y = int(position[1])
    self._dirx = float(direction_vector[0])
    self._diry = float(direction_vector[1])

  @property
  def x(self):
    return self._x
  @x.setter
  def x(self, value):
    self._x = value

  @property
  def y(self):
    return self._y
  @y.setter
  def y(self, value):
    self._y = value

  @property
  def dirx(self):
    return self._dirx
  @dirx.setter
  def dirx(self, value):
    self._dirx = value

  @property
  def diry(self):
    return self._diry
  @diry.setter
  def diry(self, value):
    self._diry = value

  @property
  def planex(self):
    return float(0.7 * -self._diry)

  @property
  def planey(self):
    return float(0.7 * self._dirx)

  def rotate(self, direction):
    old_dirx = self.dirx
    direction = direction * math.pi / 2
    self._dirx = int(self._dirx * math.cos(direction) - self._diry * math.sin(direction))
    self._diry = int(old_dirx * math.sin(direction) + self._diry * math.cos(direction))