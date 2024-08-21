"""
from https://pygame.me/docs/
Breakout by JohnnyBGuud
"""
import pygame.sprite

from settings import *

class Game:
    def __init__(self):
        # setup
        pygame.init()
        self.display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Breakout")
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # sprites
        self.player = Player((400,300), self.all_sprites, self.collision_sprites)
