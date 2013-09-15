import sys
import pdb
import pygame
import crawler

from pygame.locals import *
from crawler.locals import *

def main():
  pygame.init()
  pygame.display.set_caption("Dung crawler")
  window = pygame.display.set_mode(SCR_SIZE)
  screen = pygame.display.get_surface()
  map_01 = crawler.map.Map()
  renderer = crawler.renderer.Renderer(screen, map_01)

  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        return
      elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          return
      else:
        pass
    pygame.display.update()
    renderer.render()

if __name__ == '__main__':
    main()