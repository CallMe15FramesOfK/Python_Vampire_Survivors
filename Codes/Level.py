import pygame
import PyGAME_objects
from Text import Text


class Level:
    def __init__(self, player):
        self.player = player
        self.set_of_enemies = pygame.sprite.Group()
        self.set_of_bullets = pygame.sprite.Group()

        player.score = 0
        player.health_bar.hp = 100
        player.rect.center = PyGAME_objects.screen.get_rect().center

        self.score_text = Text(self.player.score, "violet", PyGAME_objects.WIDTH * 0.5, 50, 60, 'Ariel')

    def update(self):
        self.set_of_bullets.update()
        self.set_of_enemies.update()

        self.score_text.text = str(self.player.score)

        for e in self.set_of_enemies:
            if e.rect.top > PyGAME_objects.HEIGHT:
                e.kill()

        for b in self.set_of_bullets:
            if b.rect.bottom < 0:
                b.kill()
            for m in pygame.sprite.spritecollide(b, self.set_of_enemies, True):
                b.kill()
                self.player.score += 5

    def draw(self, surface):
        surface.blit(PyGAME_objects.GAME_GRASS, (0, 0))
        self.set_of_enemies.draw(surface)
        self.set_of_bullets.draw(surface)
        self.score_text.draw(PyGAME_objects.screen)
