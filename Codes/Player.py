import pygame
import PyGAME_objects
from Attack import Mine


class HealthBar:

    def __init__(self, x, y, width, height, max_hp):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(PyGAME_objects.screen, 'red', (self.x, self.y, self.w, self.h))
        if self.hp > 100:
            pygame.draw.rect(PyGAME_objects.screen, 'blue', (self.x, self.y, self.w * ratio, self.h))
        else:
            pygame.draw.rect(PyGAME_objects.screen, 'green', (self.x, self.y, self.w * ratio, self.h))


class Player(pygame.sprite.Sprite):
    coor = []

    def __init__(self, image, cx, cy):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = cx, cy
        self.level = None
        self.score = 0
        self.health_bar = HealthBar(0, 0, 300, 40, 100)

    def _get_event(self, key_pressed):
        if key_pressed[pygame.K_LEFT]:
            self.rect.move_ip([-6, 0])
        if key_pressed[pygame.K_RIGHT]:
            self.rect.move_ip([6, 0])
        if key_pressed[pygame.K_UP]:
            self.rect.move_ip([0, -6])
        if key_pressed[pygame.K_DOWN]:
            self.rect.move_ip([0, 6])
        if key_pressed[pygame.K_SPACE]:
            self._shoot()
        if key_pressed[pygame.K_h]:
            self._heal()

    def update(self, key_pressed):
        self._get_event(key_pressed)
        # wyjęcie poza krawędzie ekranu
        if self.rect.centerx < 0:
            self.rect.centerx = 0
        if self.rect.centerx > PyGAME_objects.WIDTH:
            self.rect.centerx = PyGAME_objects.WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > PyGAME_objects.HEIGHT:
            self.rect.bottom = PyGAME_objects.HEIGHT

        self.__class__.coor.append([self.rect.x, self.rect.y])
        if len(self.__class__.coor) > 6:
            del self.__class__.coor[0]

        for l in pygame.sprite.spritecollide(self, self.level.set_of_enemies, False):
            self.health_bar.hp -= 0.4

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def _shoot(self):
        if not pygame.sprite.spritecollide(self, self.level.set_of_bullets, False) and len(
                self.level.set_of_bullets) < 5:
            b1 = Mine([PyGAME_objects.IMAGES['BULLET']], self.rect.centerx, self.rect.centery - 40)
            self.level.set_of_bullets.add(b1)

    def _heal(self):
        if self.score >= 100 and self.health_bar.hp < 200:
            self.health_bar.hp += self.health_bar.max_hp * 0.40
            self.score -= 100
        else:
            pass
