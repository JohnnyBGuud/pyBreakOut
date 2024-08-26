"""
from https://pygame.me/docs/
Breakout by JohnnyBGuud
"""

from settings import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill('yellow')
        self.rect = self.image.get_frect(center = pos)

        # movement
        self.direction = pygame.Vector2()
        self.speed = 500
        self.collision_sprites = collision_sprites

    def move(self, dt):
        if self.rect.right > WINDOW_WIDTH:
            self.direction.x *= -1
            self.rect.right = WINDOW_WIDTH
        if self.rect.left < 0:
            self.direction.x *= -1
            self.rect.left = 0
        if self.rect.top < 0:
            self.direction.y *= -1
            self.rect.top = 0
        if self.rect.y > WINDOW_HEIGHT:
            self.kill()
            pygame.quit()
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt

    def bounce(self, ballposx, paddleposx, paddleposy):
        self.direction.y *= -1
        self.direction.x = (ballposx - paddleposx)/100

    def update(self, dt):
        self.move(dt)

class Brick(pygame.sprite.Sprite):
    def __init__(self, color, size, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_frect(center=(pos))
