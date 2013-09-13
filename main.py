import sys
import pygame
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 640,480

def main():
  pygame.init()
  window = pygame.display.set_mode(SIZE)
  pygame.display.set_caption("Dung crawler")
  pygame.mouse.set_visible(False)

  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        return
      elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          return
    pygame.display.update()

if __name__ == '__main__':
    main()