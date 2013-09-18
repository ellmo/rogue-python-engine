import pygame
import math

import camera
import crawler_map
from locals import *

class Renderer(object):
  def __init__(self, surface, crawler_map):
    self._camera = camera.Camera(crawler_map.start_position, 0, -1)
    self._surface = surface
    self._map = crawler_map
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
      cameraX = float(2 * x_column / float(self._width) - 1) #x-coordinate in camera space
      rayPosX = self._camera.x + 0.5
      rayPosY = self._camera.y + 0.5
      rayDirX = self._camera.dirx + self._camera.planex * cameraX
      rayDirY = self._camera.diry + self._camera.planey * cameraX
      mapX = int(rayPosX)
      mapY = int(rayPosY)

      # import pdb; pdb.set_trace()

      #length of ray from current position to next x or y-side
      sideDistX = 0.
      sideDistY = 0.

      #length of ray from one x or y-side to next x or y-side
      if rayDirX == 0: rayDirX = 0.00001
      if rayDirY == 0: rayDirY = 0.00001
      deltaDistX = math.sqrt(1 + (rayDirY**2) / (rayDirX**2))
      deltaDistY = math.sqrt(1 + (rayDirX**2) / (rayDirY**2))
      perpWallDist = 0.

      #what direction to step in x or y-direction (either +1 or -1)
      stepX = 0
      stepY = 0

      hit = 0 #was there a wall hit?
      side = 0 # was a NS or a EW wall hit?

      # calculate step and initial sideDist
      if rayDirX < 0:
        stepX = -1
        sideDistX = (rayPosX - mapX) * deltaDistX
      else:
        stepX = 1
        sideDistX = (mapX + 1.0 - rayPosX) * deltaDistX

      if rayDirY < 0:
        stepY = -1
        sideDistY = (rayPosY - mapY) * deltaDistY
      else:
        stepY = 1
        sideDistY = (mapY + 1.0 - rayPosY) * deltaDistY

      # perform DDA
      while hit == 0:
        # jump to next map square, OR in x - direction, OR in y - direction
        # import pdb; pdb.set_trace()
        if sideDistX < sideDistY:
          sideDistX += deltaDistX
          mapX += stepX
          side = 0
        else:
          sideDistY += deltaDistY
          mapY += stepY
          side = 1
        # Check if ray has hit a wall
        tile = self._map.tiles[mapY][mapX]
        if tile.solid:
            hit = 1
      # Calculate distance projected on camera direction (oblique distance will give fisheye effect !)
      if (side == 0):
        perpWallDist = (abs((mapX - rayPosX + (1 - stepX) / 2) / rayDirX))
      else:
        perpWallDist = (abs((mapY - rayPosY + (1 - stepY) / 2) / rayDirY))

      # Calculate height of line to draw on surface
      if perpWallDist == 0:perpWallDist = 0.000001
      lineHeight = abs(int(self._height / perpWallDist))

      # calculate lowest and highest pixel to fill in current stripe
      drawStart = - lineHeight / 2 + self._height / 2
      drawEnd = lineHeight / 2 + self._height / 2

      #calculate value of wallX
      wallX = 0 #where exactly the wall was hit
      if (side == 1):
        wallX = rayPosX + ((mapY - rayPosY + (1 - stepY) / 2) / rayDirY) * rayDirX
      else:
        wallX = rayPosY + ((mapX - rayPosX + (1 - stepX) / 2) / rayDirX) * rayDirY;
      wallX -= math.floor((wallX));

      #x coordinate on the texture
      texX = int(wallX * float(TEX_SIZE))
      if(side == 0 and rayDirX > 0):
        texX = TEX_SIZE - texX - 1;
      if(side == 1 and rayDirY < 0):
        texX = TEX_SIZE - texX - 1;

      if lineHeight > 1000:
        lineHeight=1000
        drawStart = -1000 /2 + self._height/2
      if not tile.texture is None:
        img = tile.texture.converted if side == 0 else tile.texture.converted_darkened
        self._surface.blit(pygame.transform.scale(img[texX], (1, lineHeight)), (x_column, drawStart))