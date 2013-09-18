import sys
import pygame
import crawler

from pygame.locals import *
from crawler.locals import *

def main():
  pygame.init()
  pygame.display.set_caption("Dung crawler")

  window = pygame.display.set_mode(SCR_SIZE)
  screen = pygame.display.get_surface()

  map_01 = crawler.crawler_map.CrawlerMap()
  renderer = crawler.renderer.Renderer(screen, map_01)

  while True:
    game_clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        return
      elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          return
      else:
        pass
    renderer.render()
    print str(game_clock.get_fps())
    pygame.display.update()

if __name__ == '__main__':
    main()