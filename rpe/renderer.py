import pygame
import math

import camera
import rpe_map
from locals import *

class Renderer(object):
  def __init__(self, surface, rpe_map, camera):
    self._camera = camera
    self._surface = surface
    self._map = rpe_map
    self._width = self._surface.get_width()
    self._height = self._surface.get_height()
    self._background = pygame.transform.scale(
      pygame.image.load("res/bkg.png").convert(),
      (self._width, self._height)
    )

  @property
  def surface(self):
    return self._surface

  @property
  def camera(self):
    return self._camera

  def render(self):
    self._surface.blit(self._background, (0, 0))

  def raycast(self):
    # Raycasting + DDA algorithm
    # based on http://lodev.org/cgtutor/raycasting.html
    for x_column in range(self._width):
      #calculate ray position and direction
      camera_x = float(2 * x_column / float(self._width) - 1) #x-coordinate in camera space
      ray_posx = self._camera.x + 0.5 - (self._camera.dirx * 0.75)
      ray_posy = self._camera.y + 0.5 - (self._camera.diry * 0.75)
      ray_dirx = self._camera.dirx + self._camera.planex * camera_x
      ray_diry = self._camera.diry + self._camera.planey * camera_x
      mapx = int(ray_posx)
      mapy = int(ray_posy)

      #length of ray from current position to next x or y-side
      side_dist_x = 0.
      side_dist_y = 0.

      #length of ray from one x or y-side to next x or y-side
      if ray_dirx == 0: ray_dirx = 0.00001
      if ray_diry == 0: ray_diry = 0.00001
      delta_dist_x = math.sqrt(1 + (ray_diry**2) / (ray_dirx**2))
      delta_dist_y = math.sqrt(1 + (ray_dirx**2) / (ray_diry**2))
      perpendicular_wall_dist = 0.

      #what direction to step in x or y-direction (either +1 or -1)
      stepX = 0
      stepY = 0

      hit = 0 #was there a wall hit?
      side = 0 # was a NS or a EW wall hit?

      # calculate step and initial sideDist
      if ray_dirx < 0:
        stepX = -1
        side_dist_x = (ray_posx - mapx) * delta_dist_x
      else:
        stepX = 1
        side_dist_x = (mapx + 1.0 - ray_posx) * delta_dist_x

      if ray_diry < 0:
        stepY = -1
        side_dist_y = (ray_posy - mapy) * delta_dist_y
      else:
        stepY = 1
        side_dist_y = (mapy + 1.0 - ray_posy) * delta_dist_y

      # perform Digital Differential Analysis
      while hit == 0:
        # jump to next map square, OR in x - direction, OR in y - direction
        if side_dist_x < side_dist_y:
          side_dist_x += delta_dist_x
          mapx += stepX
          side = 0
        else:
          side_dist_y += delta_dist_y
          mapy += stepY
          side = 1
        # Check if ray has hit a wall
        tile = self._map.tiles[mapy][mapx]
        if tile.solid:
          hit = 1
      # Calculate distance projected on camera direction (oblique distance will give fisheye effect !)
      if (side == 0):
        perpendicular_wall_dist = (abs((mapx - ray_posx + (1 - stepX) / 2) / ray_dirx))
      else:
        perpendicular_wall_dist = (abs((mapy - ray_posy + (1 - stepY) / 2) / ray_diry))

      # Calculate height of line to draw on surface
      if perpendicular_wall_dist == 0: perpendicular_wall_dist = 0.000001
      lineHeight = abs(int(self._height / perpendicular_wall_dist))

      # calculate lowest and highest pixel to fill in current stripe
      draw_start = - lineHeight / 2 + self._height / 2
      draw_end = lineHeight / 2 + self._height / 2

      #calculate value of wall_x
      wall_x = 0 #where exactly the wall was hit
      if (side == 1):
        wall_x = ray_posx + ((mapy - ray_posy + (1 - stepY) / 2) / ray_diry) * ray_dirx
      else:
        wall_x = ray_posy + ((mapx - ray_posx + (1 - stepX) / 2) / ray_dirx) * ray_diry
      wall_x -= math.floor((wall_x));

      #x coordinate on the texture
      tex_x = int(wall_x * float(TEX_SIZE))
      if(side == 0 and ray_dirx > 0):
        tex_x = TEX_SIZE - tex_x - 1;
      if(side == 1 and ray_diry < 0):
        tex_x = TEX_SIZE - tex_x - 1;

      if lineHeight > 1000:
        lineHeight=1000
        draw_start = -1000 /2 + self._height/2
      if not tile.texture is None:
        img = tile.texture.converted if side == 0 else tile.texture.converted_darkened
        self._surface.blit(pygame.transform.scale(img[tex_x], (1, lineHeight)), (x_column, draw_start))