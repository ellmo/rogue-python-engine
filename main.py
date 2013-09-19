import sys
import pygame
import rpe

from pygame.locals import *
from rpe.locals import *

def main():
  pygame.init()
  pygame.display.set_caption("Rogue Python Engine")

  game_clock = pygame.time.Clock()

  window = pygame.display.set_mode(SCR_SIZE)
  screen = pygame.display.get_surface()

  map_01 = rpe.rpe_map.RpeMap('res/map01.rpe')
  player = rpe.player.Player(map_01, (0, -1))
  renderer = rpe.renderer.Renderer(screen, map_01, player.camera)

  while True:
    game_clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        return
      elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          return
        elif event.key == K_w:
          player.move(1, 0)
        elif event.key == K_s:
          player.move(-1, 0)
        elif event.key == K_q:
          player.move(0, 1)
        elif event.key == K_e:
          player.move(0, -1)
        elif event.key == K_a:
          player.rotate(-1)
        elif event.key == K_d:
          player.rotate(1)
      else:
        pass
    renderer.render()
    #print str(game_clock.get_fps())
    pygame.display.update()

if __name__ == '__main__':
    main()