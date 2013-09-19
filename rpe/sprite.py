import pdb
import pygame

import texture

from locals import *

class Sprite(texture.Texture):
  def __init__(self, image_path='res/barrel.png'):
    super(Sprite, self).__init__(image_path)
