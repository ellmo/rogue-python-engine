import pdb
import math

class Camera(object):
  def __init__(self, position, dirx, diry, planex, planey):
    self._y = float(position[0])
    self._x = float(position[1])
    self._dirx = float(dirx)
    self._diry = float(diry)
    self._planex = float(planex)
    self._planey = float(planey)

  @property
  def x(self):
    return self._x

  @property
  def y(self):
    return self._y




