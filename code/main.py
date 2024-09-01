"""
from https://pygame.me/docs/
Breakout by JohnnyBGuud
"""

from settings import *
from player import Paddle
from player import Ball
from sprites import *
from random import random
import colorsys

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
        self.paddle = Paddle((WINDOW_WIDTH/2, WINDOW_HEIGHT - 10), (self.all_sprites))
        self.ball = Ball((WINDOW_WIDTH/2, WINDOW_HEIGHT - 30), (10, 10), self.all_sprites, self.collision_sprites)
        self.ball.direction.x = random()
        self.ball.direction.y = -1
        # brick columns:
        for i in range(10):
            width = WINDOW_WIDTH/10 - WINDOW_WIDTH/50
            height = 50
            dist = WINDOW_WIDTH/10
            # brick rows:
            for j in range(6):
                color = pygame.Color(0,0,0)
                color.hsva = (j * 50, 100, 100, 100)
                Brick((color), (width, height), (dist / 2 + i * dist, height * (j * 1.5 + 0.5) + 10),
                      (self.all_sprites, self.collision_sprites))

        # score
        self.score = {'player': 0}
        self.font = pygame.font.Font(None, 30)

    def display_score(self):
        player_surf = self.font.render(str(f'SCORE: {self.score['player']}'), True, 'white')
        player_rect = player_surf.get_rect(center = (WINDOW_WIDTH - 60, WINDOW_HEIGHT - 10))
        self.display_surf.blit(player_surf, player_rect)

    def run(self):
        while self.running:
            # dt
            dt = self.clock.tick(60) / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            self.all_sprites.update(dt)

            # collision
            if pygame.sprite.collide_rect(self.ball, self.paddle):
                self.ball.bounce(self.ball.rect.centerx, self.paddle.rect.centerx, self.paddle.rect.top)

            self.brick_collision_list = pygame.sprite.spritecollide(self.ball, self.collision_sprites, False)
            for brick in self.brick_collision_list:
                self.ball.collision(brick.rect.centery, brick.rect.height, brick.rect.centerx, brick.rect.width)
                brick.kill()
                self.score['player'] += 1

            # draw
            self.display_surf.fill((0, 0, 0))
            self.all_sprites.draw(self.display_surf)
            self.display_score()
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()

