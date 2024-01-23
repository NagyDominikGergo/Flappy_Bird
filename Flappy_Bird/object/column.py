import random
import pygame.sprite
import assets
import configs
from object.layer import Layer


class Column(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.OBSTACLE
        self.gap = 100
        self.random = random.randint(0, 200)

        self.sprite = assets.get_sprite("pipe-green")
        self.sprite_rect = self.sprite.get_rect()

        self.pipe_bottom = self.sprite
        self.pipe_bottom_rect = self.pipe_bottom.get_rect(bottomleft=(0, configs.SCREEN_HEIGHT + self.random))

        self.pipe_top = pygame.transform.flip(self.sprite, False, True)
        self.pipe_top_rect = self.pipe_top.get_rect(bottomleft=(0, self.random + self.gap))

        self.image = pygame.surface.Surface((self.sprite_rect.width, self.sprite_rect.height * 2 + self.gap),
                                            pygame.SRCALPHA)
        self.image.blit(self.pipe_bottom, self.pipe_bottom_rect)
        self.image.blit(self.pipe_top, self.pipe_top_rect)

        self.rect = self.image.get_rect(midleft=(configs.SCREEN_WIDTH, 350))

        self.mask = pygame.mask.from_surface(self.image)
        self.passed = False

        super().__init__(*groups)

    def update(self):
        self.rect.x -= 2

        if self.rect.right <= 0:
            self.kill()

    def is_passed(self):
        if self.rect.x < 20 and not self.passed:
            self.passed = True
            return True
        return False

