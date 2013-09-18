import crawler_map
import camera

class Player(object):
  def __init__(self, crawler_map, direction_vector):
    self._crawler_map = crawler_map
    self._x = crawler_map.start_position[0]
    self._y = crawler_map.start_position[1]
    self._camera = camera.Camera(crawler_map.start_position, direction_vector)
    print "player is at {0}, {1}".format(self._x, self._y)

  @property
  def crawler_map(self):
    return self._crawler_map

  @property
  def camera(self):
    return self._camera

  @property
  def x(self):
    return self._x

  @property
  def y(self):
    return self._y

  @property
  def position(self):
    return (self._x, self._y)

  @property
  def dirx(self):
    return self._camera.dirx

  @property
  def diry(self):
    return self._camera.diry

  def move(self, forward, left):
    if left is 0:
      self._x += self.dirx * forward
      self._y += self.diry * forward
    else:
      self._x += self.diry * left
      self._y -= self.dirx * left
    self._camera.x = self._x
    self._camera.y = self._y
    print "player moved to {0}, {1}".format(self._x, self._y)

  def rotate(self, direction):
    self._camera.rotate(direction)

