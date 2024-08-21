"""
from https://pygame.me/docs/
Breakout by JohnnyBGuud
"""

from settings import *

class CollisionSprites(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill('blue')
        self.rect = self.image.get_frect(center = pos)

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
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt
        if self.rect.x >= WINDOW_WIDTH or self.rect.x <= 0:
            self.direction.x *= -1
        if self.rect.y <= 0:
            self.direction.y *= -1
        if self.rect.y >= WINDOW_HEIGHT:
            self.kill()
        self.bounce()

    def bounce(self):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                self.direction.y *= -1

    def update(self, dt):
        self.move(dt)
