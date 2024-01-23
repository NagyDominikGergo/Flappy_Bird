import pygame.sprite

import assets
import configs
from object.column import Column
from object.floor import Floor
from object.layer import Layer


class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.OBSTACLE
        self.flap = 0

        self.images = [
            assets.get_sprite("redbird-upflap"),
            assets.get_sprite("redbird-midflap"),
            assets.get_sprite("redbird-downflap")
        ]

        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(20, 50))
        self.mask = pygame.mask.from_surface(self.image)
        #self.rect = self.image.get_rect(midleft=(configs.SCREEN_WIDTH / 2 - 25, configs.SCREEN_HEIGHT / 2))
        super().__init__(*groups)

    def update(self, *args, **kwargs):
        self.images.append(self.images.pop(0))
        self.image = self.images[0]
        #self.image = pygame.transform.rotate(self.image, -45)

        self.flap += configs.GRAVITY
        self.rect.y += self.flap

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #self.image = pygame.transform.rotate(self.image, 45)
            self.flap = 0
            self.flap -= 5
            assets.play_audio("wing")

    def check_collision(self, sprites):
        for sprite in sprites:
            if ((type(sprite) is Column or type(sprite) is Floor) and
                    sprite.mask.overlap(self.mask, (self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y)) or self.rect.top < 0):
                return True
        return False
