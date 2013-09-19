import math
import pygame

from locals import *

class Ray(object):
  def __init__(self, renderer, x_column):
    self._renderer = renderer
    self._x_column = x_column
    self._camera = renderer.camera
    self._map = renderer.rpe_map
    # get the directional vector of the ray
    camera_x = float(2 * x_column / float(self._renderer.width) - 1) # x-coordinate in camera space
    self._ray_dirx = self._camera.dirx + self._camera.planex * camera_x
    self._ray_diry = self._camera.diry + self._camera.planey * camera_x
    if self._ray_dirx == 0: self._ray_dirx = 0.00001
    if self._ray_diry == 0: self._ray_diry = 0.00001
    # set the anchor point of the camera and then puch it back a little
    # so that it sees floor of the current cell.
    self._ray_posx = self._camera.x + 0.5 - (self._camera.dirx * 0.75)
    self._ray_posy = self._camera.y + 0.5 - (self._camera.diry * 0.75)
    self._delta_dist_x = math.sqrt(1 + (self._ray_diry**2) / (self._ray_dirx**2))
    self._delta_dist_y = math.sqrt(1 + (self._ray_dirx**2) / (self._ray_diry**2))
    self._mapx = int(self._camera.x)
    self._mapy = int(self._camera.y)
    #
    self._hit = 0  # has the ray hit the wall?
    self._side = 0 # which side NS or WE was hit?
    #
    self._side_dist_x = 0.
    self._side_dist_y = 0.
    #
    self._tile = None # which tile was hit?
    self._wall_distance = 0. # what is the distance to the wall?
    self._wall_x = 0. # where exactly the wall was hit horizontally?
    self._line_height = 0. # how tall is the portion of the wall hit by ray?
    self._draw_start = 0. # where on the screen does the vertical line start and end?
    self._texture_x = 0. # what vertical part of the texture are we talking about?
    #
    self.__perform_dda()
    self.__calculate_wall_distance()
    self.__calculate_wall_x()
    self.__calculate_wall_y()
    self.__calculate_texture_x()

  @property
  def tile(self):
    return self._tile

  @property
  def side(self):
    return self._side

  @property
  def wall_x(self):
    return self._wall_x

  @property
  def line_height(self):
    return self._line_height

  @property
  def draw_start(self):
    return self._draw_start

  @property
  def texture_x(self):
    return self._texture_x

  def render_texture(self):
    if not self._tile.texture is None:
      img = self._tile.texture.converted if self._side == 0 else self._tile.texture.converted_darkened
      self._renderer.surface.blit(pygame.transform.scale(
        img[self._texture_x],
        (1, self._line_height)),
        (self._x_column, self._draw_start))

  # private methods

  def __perform_dda(self):
    # what direction to step in x or y-direction (either +1 or -1)
    self._step_x = 0
    self._step_y = 0
    # calculate step and initial sideDist
    if self._ray_dirx < 0:
      self._step_x = -1
      self._side_dist_x = (self._ray_posx - self._mapx) * self._delta_dist_x
    else:
      self._step_x = 1
      self._side_dist_x = (self._mapx + 1.0 - self._ray_posx) * self._delta_dist_x

    if self._ray_diry < 0:
      self._step_y = -1
      self._side_dist_y = (self._ray_posy - self._mapy) * self._delta_dist_y
    else:
      self._step_y = 1
      self._side_dist_y = (self._mapy + 1.0 - self._ray_posy) * self._delta_dist_y
    self.__detect_hit()

  def __detect_hit(self):
    while self._hit is 0:
      # jump to next map square, OR in x - direction, OR in y - direction
      if self._side_dist_x < self._side_dist_y:
        self._side_dist_x += self._delta_dist_x
        self._mapx += self._step_x
        self._side = 0
      else:
        self._side_dist_y += self._delta_dist_y
        self._mapy += self._step_y
        self._side = 1
      # Check if ray has hit a wall
      self._tile = self._map.tiles[self._mapy][self._mapx]
      if self._tile.solid:
        self._hit = 1

  def __calculate_wall_distance(self):
    # Calculate distance projected on camera direction (oblique distance will give fisheye effect !)
    if (self._side == 0):
      self._wall_distance = (abs((self._mapx - self._ray_posx + (1 - self._step_x) / 2) / self._ray_dirx))
    else:
      self._wall_distance = (abs((self._mapy - self._ray_posy + (1 - self._step_y) / 2) / self._ray_diry))
    if self._wall_distance == 0: self._wall_distance = 0.000001

  def __calculate_wall_x(self):
    # Calculate which horizontal part of the wall was hit
    if (self._side == 1):
      self._wall_x = self._ray_posx + ((self._mapy - self._ray_posy + (1 - self._step_y) / 2) / self._ray_diry) * self._ray_dirx
    else:
      self._wall_x = self._ray_posy + ((self._mapx - self._ray_posx + (1 - self._step_x) / 2) / self._ray_dirx) * self._ray_diry
    self._wall_x -= math.floor((self._wall_x));

  def __calculate_wall_y(self):
    # Calculate height of line to draw on surface and the lowest pixel to fill in current stripe
    self._line_height = abs(int(self._renderer.height / self._wall_distance))
    self._draw_start = -self._line_height / 2 + self._renderer.height / 2
    if self._line_height > 1000:
      self._line_height = 1000
      self._draw_start = -1000 /2 + self._renderer.height/2

  def __calculate_texture_x(self):
    # Calculate which horizontal part (offser) of the texture to draw
    self._texture_x = int(self._wall_x * float(TEX_SIZE))
    if(self._side == 0 and self._ray_dirx > 0):
      self._texture_x = TEX_SIZE - self._texture_x - 1;
    if(self._side == 1 and self._ray_diry < 0):
      self._texture_x = TEX_SIZE - self._texture_x - 1;