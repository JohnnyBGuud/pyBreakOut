"""
from https://pygame.me/docs/
Breakout by JohnnyBGuud
"""

from settings import *
from player import Player
from sprites import *

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
        self.player = Player((WINDOW_WIDTH/2, WINDOW_HEIGHT - 10), (self.all_sprites, self.collision_sprites))
        self.ball = Ball((WINDOW_WIDTH/2, WINDOW_HEIGHT - 30), (10, 10), self.all_sprites, self.collision_sprites)
        self.ball.direction.x = 1
        self.ball.direction.y = -1
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

            # draw
            self.display_surf.fill((0, 0, 0))
            self.all_sprites.draw(self.display_surf)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()

