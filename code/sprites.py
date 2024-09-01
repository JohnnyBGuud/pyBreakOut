"""
from https://pygame.me/docs/
Breakout by JohnnyBGuud
"""

from settings import *
pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 20)


class Brick(pygame.sprite.Sprite):
    def __init__(self, color, size, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_frect(center=(pos))

