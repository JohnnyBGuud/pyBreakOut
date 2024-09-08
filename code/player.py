"""
from https://pygame.me/docs/
Breakout by JohnnyBGuud
"""

from settings import *


class Paddle(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface((200, 20))
        self.image.fill('white')
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT - 10), )

        # movement
        self.direction = pygame.Vector2()
        self.speed_x = 500
        self.speed_y = 250

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed_x * dt
        self.rect.y += self.direction.y * self.speed_y * dt
        if self.rect.right >= WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0

    def increase_speed(self):
        self.speed_x += 10

    def update(self, dt):
        self.input()
        self.move(dt)


class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, collision_sprites):
        super().__init__(groups)
        self.collision_sprites = collision_sprites
        # image
        self.image = pygame.Surface((10, 10))
        self.image.fill('yellow')

        # rect
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT - 30))
        self.old_rect = self.rect.copy()

        # movement
        self.direction = pygame.Vector2()
        self.speed = 300

    def move(self, dt):
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
            self.direction.x *= -1

        if self.rect.left < 0:
            self.rect.left = 0
            self.direction.x *= -1

        if self.rect.top < 0:
            self.rect.top = 0
            self.direction.y *= -1

        if self.rect.y > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.direction.y *= -1
            # self.kill()
            # self.reset()

        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt

    def reset(self):
        self.speed = 300
        self.direction.x = random()
        self.direction.y = -1

    def collision(self, brick):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.rect.right > brick.rect.left >= self.old_rect.right:
                    self.rect.right = brick.rect.left
                    self.direction.x *= -1
                if self.rect.bottom > brick.rect.top >= self.old_rect.bottom:
                    self.rect.bottom = brick.rect.top
                    self.direction.y *= -1
                if self.rect.left < brick.rect.right <= self.old_rect.left:
                    self.rect.left = brick.rect.right
                    self.direction.x *= -1
                if self.rect.top < brick.rect.bottom <= self.old_rect.top:
                    self.rect.top = brick.rect.bottom
                    self.direction.y *= -1

    def bounce(self, paddle):
        self.speed += 10
        self.direction.y *= -1
        if self.rect.right > paddle.rect.left >= self.old_rect.right:
            self.rect.right = paddle.rect.left
        if self.rect.left < paddle.rect.right <= self.old_rect.left:
            self.rect.left = paddle.rect.right
        if self.rect.bottom > paddle.rect.top >= self.old_rect.bottom:
            self.rect.bottom = paddle.rect.top
        if self.rect.top < paddle.rect.top <= self.old_rect.bottom:
            self.rect.top = paddle.rect.bottom
        self.direction.x = (self.rect.centerx - paddle.rect.centerx) / 100

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.move(dt)
