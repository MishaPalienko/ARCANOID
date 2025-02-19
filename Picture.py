import pygame
from Area import Area
from Area import mw

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        super().__init__(x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (width, height))

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))