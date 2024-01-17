import pygame


class Mine(pygame.sprite.Sprite):
    def __init__(self, images, cx, cy):
        super().__init__()
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = cx, cy
