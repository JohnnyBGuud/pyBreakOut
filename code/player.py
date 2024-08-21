

from settings import *

class Player:
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.Surface((400, 200))
        ((400,300), self.all_sprites, self.collision_sprites)