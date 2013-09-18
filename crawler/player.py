import crawler_map
import camera

class Player(object):
  def __init__(self, crawler_map, direction_vector):
    self._crawler_map = crawler_map
    self._position = (crawler_map.start_position[0], crawler_map.start_position[1])
    self._camera = camera.Camera(self._position, direction_vector)

  @property
  def crawler_map(self):
    return self._crawler_map

  @property
  def camera(self):
    return self._camera

  @property
  def x(self):
    return self._position[0]

  @property
  def y(self):
    return self._position[1]

  @property
  def dirx(self):
    return self._camera.dirx

  @property
  def diry(self):
    return self._camera.diry

  def move(self, vector):
    self._x = vector[0]
    self._camera.x = vector[0]
    self._y = vector[1]
    self._camera.y = vector[1]


  def rotate(self, vector):
    self._camera.dirx = vector[0]
    self._camera.diry = vector[1]

