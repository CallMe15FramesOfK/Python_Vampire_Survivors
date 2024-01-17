import os
import pygame

pygame.init()

# stałe
SIZESCREEN = WIDTH, HEIGHT = 1366, 740

screen = pygame.display.set_mode(SIZESCREEN)
clock = pygame.time.Clock()


# wczytywanie grafik
path = os.path.join(os.pardir, 'images')
file_names = sorted(os.listdir(path))
BACKGROUND = pygame.image.load(os.path.join(path, 'menu_background.png')).convert()
file_names.remove('menu_background.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, SIZESCREEN)
GAME_GRASS = pygame.image.load(os.path.join(path, 'level_background.png')).convert()
file_names.remove('level_background.png')


IMAGES = {}
for file_name in file_names:
    IMAGES[file_name[:-4].upper()] = pygame.image.load(
        os.path.join(path, file_name)).convert_alpha(BACKGROUND)
