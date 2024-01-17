import pygame
import PyGAME_objects

from Player import Player
from Button import Button

from First_Level import First_Level
from Text import Text

start_button = Button(430, 150, PyGAME_objects.IMAGES['NEW_GAME_BUTTON'])
quit_button = Button(1070, 0, PyGAME_objects.IMAGES['QUIT_BUTTON'])
exit_button = Button(400, 450, PyGAME_objects.IMAGES['EXIT_BUTTON'])
player = Player(PyGAME_objects.IMAGES['PLAYER'], *PyGAME_objects.screen.get_rect().center)
Score_text = Text('Score : ', 'pink', 500, 370, 120, 'Arial')

main_menu = True
window_open = True

while window_open:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
        elif event.type == pygame.QUIT:
            window_open = False

    if player.health_bar.hp < 0:
        break

    key_pressed = pygame.key.get_pressed()
    PyGAME_objects.screen.blit(PyGAME_objects.BACKGROUND, (0, 0))
    if main_menu:
        if start_button.draw():
            main_menu = False
            current_level = First_Level(player)
            player.level = current_level
        if exit_button.draw():
            exit()
    else:
        PyGAME_objects.screen.blit(PyGAME_objects.GAME_GRASS, (0, 0))
        current_level.draw(PyGAME_objects.screen)
        player.draw(PyGAME_objects.screen)
        player.health_bar.draw(PyGAME_objects.screen)
        current_level.update()
        player.update(key_pressed)
        if quit_button.draw():
            main_menu = True

    pygame.display.update()
    pygame.display.flip()
    PyGAME_objects.clock.tick(60)

Score = Text(player.score, 'pink', 850, 370, 120, 'Arial')
pygame.time.delay(500)
PyGAME_objects.screen.fill("violet")
Score_text.draw(PyGAME_objects.screen)
Score.draw(PyGAME_objects.screen)
pygame.display.flip()
pygame.time.delay(2000)
pygame.quit()
