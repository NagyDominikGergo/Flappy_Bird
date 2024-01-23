import pygame

import assets
import configs

from object.background import Background
from object.bird import Bird
from object.column import Column
from object.floor import Floor
from object.game_over_message import GameOverMessage
from object.game_start_message import GameStartMessage
from object.score import Score

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
column_creat_event = pygame.USEREVENT
click_user_event = pygame.event.get()
running = True
gameover = False
game_started = False

assets.load_sprites()
assets.load_audios()

sprites = pygame.sprite.LayeredUpdates()

Background(0, sprites)
Background(1, sprites)

Floor(0, sprites)
Floor(1, sprites)

gamestart = GameStartMessage(sprites)
score = Score(sprites)
bird = Bird(sprites)

pygame.time.set_timer(column_creat_event, 1500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == column_creat_event and game_started is True:
            Column(sprites)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_started = True
                #score = Score(sprites)

        bird.handle_event(event)

    screen.fill(0)
    sprites.draw(screen)

    if not gameover and game_started:
        sprites.update()
        gamestart.update()

    if bird.check_collision(sprites) and not gameover:
        gameover = True
        GameOverMessage(sprites)
        game_started = False
        assets.play_audio("hit")

    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score.value += 1
            assets.play_audio("point")

    #print(score)
    #score.value += 1

    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()
