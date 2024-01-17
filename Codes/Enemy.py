import pygame
import PyGAME_objects

from Player import Player


class Enemy(pygame.sprite.Sprite):
    image_list = [PyGAME_objects.IMAGES["ENEMY"]]

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

    def update(self):
        e_x = self.rect.x
        e_y = self.rect.y
        p_x = Player.coor[4][0]
        p_y = Player.coor[4][1]

        m_x, m_y = (p_x - e_x, p_y - e_y)
        m_x, m_y = (m_x / 60., m_y / 60.)

        self.rect.move_ip([m_x * 2, m_y * 2])
