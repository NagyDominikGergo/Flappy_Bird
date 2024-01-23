import pygame.sprite

import assets
import configs
from object.layer import Layer


class Score(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.UI
        self.value = 0
        self.image = pygame.surface.Surface((0, 0), pygame.SRCALPHA)
        self.scoring()
        super().__init__(*groups)

    def scoring(self):
        self.str_value = str(self.value)

        self.images = []
        self.width = 0

        for str_value_img in self.str_value:
            img = assets.get_sprite(str_value_img)
            self.images.append(img)
            self.width += img.get_width()

        self.height = self.images[0].get_height()
        self.image = pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH / 2, configs.SCREEN_HEIGHT / 2 - 200))

        pos = 0
        for img in self.images:
            self.image.blit(img, (pos, 0))
            pos += img.get_width()

    def update(self, *args, **kwargs):
        self.scoring()
