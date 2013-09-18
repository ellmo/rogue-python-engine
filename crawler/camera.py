class Camera(object):
  def __init__(self, position, dirx, diry, planex, planey):
    self._x = int(position[0])
    self._y = int(position[1])
    self._dirx = float(dirx)
    self._diry = float(diry)
    self._planex = float(planex)
    self._planey = float(planey)

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
    return self._planex
  @planex.setter
  def planex(self, value):
    self._planex = value

  @property
  def planey(self):
    return self._planey
  @planey.setter
  def planey(self, value):
    self._planey = value



