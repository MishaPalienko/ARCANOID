from Area import Area
from Area import mw
import pygame

# Класс для снаряда
class Bomb(Area):
    """Снаряд, который вылетает из монстра."""
    def __init__(self, x, y, width=80, height=80, image_path="./bomb.png"):  # Изменен размер снаряда
        super().__init__(x, y, width, height, color=None)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))

    def move(self):
        """Движение снаряда вниз."""
        self.rect.y += 5

    def draw(self):
        """Отрисовка снаряда."""
        mw.blit(self.image, (self.rect.x, self.rect.y))