import random
import pygame.sprite
from Enemy import Enemy
from Level import Level
import PyGAME_objects


class First_Level(Level):
    def __init__(self, player):
        super().__init__(player)
        self.time = 0

    def _add_enemies(self):
        image = random.choice(Enemy.image_list)
        e = Enemy(image)
        e.rect.x = random.randint(0, PyGAME_objects.WIDTH - e.rect.width)
        e.rect.y = random.randint(PyGAME_objects.HEIGHT - e.rect.height, PyGAME_objects.HEIGHT)
        if not pygame.sprite.spritecollide(e, self.set_of_enemies, False):
            self.set_of_enemies.add(e)

    def update(self):
        super().update()
        if random.randint(1, 35) == 1:
            self._add_enemies()
