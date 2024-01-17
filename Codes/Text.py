import pygame


class Text:
    def __init__(self, text, text_color, pc_x, pc_y, font_size=78, font_family=None):
        self.text = str(text)
        self.text_color = text_color
        self.font_family = font_family
        self.font_size = font_size
        self.pc_x = pc_x
        self.pc_y = pc_y
        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.update()

    def draw(self, surface):
        self.update()
        surface.blit(self.image, self.rect)

    def update(self):
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.center = self.pc_x, self.pc_y
