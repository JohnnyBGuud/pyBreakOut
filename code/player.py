"""
from https://pygame.me/docs/
Breakout by JohnnyBGuud
"""

from settings import *

class Paddle(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((200, 20))
        self.image.fill('white')
        self.rect = self.image.get_frect(center = pos)

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

    def update(self, dt):
        self.input()
        self.move(dt)


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill('yellow')
        self.rect = self.image.get_frect(center=pos)

        # movement
        self.direction = pygame.Vector2()
        self.speed = 300
        self.collision_sprites = collision_sprites

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
            # pygame.quit()
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt

    def collision(self, brick_centery, brick_height, brick_centerx, brick_width):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                # if collision is horizontal: change condition
                if (brick_centery + (brick_height / 2 - 1)) > self.rect.centery > (
                        brick_centery - (brick_height / 2 - 1)):
                    self.direction.x *= -1
                # if collision is vertical
                else:
                    self.direction.y *= -1

    def bounce(self, ballposx, paddleposx, paddleposy):
        self.speed += 10
        self.direction.y *= -1
        self.rect.bottom = paddleposy
        self.direction.x = (ballposx - paddleposx) / 100

    def update(self, dt):
        self.move(dt)
