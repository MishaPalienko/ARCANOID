from Area import Area
from Area import mw
import pygame


class Ball(Area):
  def __init__(self, filename, x, y, width, height, dx, dy):
      super().__init__(x, y, width, height)
      try:
          self.image = pygame.image.load(filename)
          self.image = pygame.transform.scale(self.image, (width, height))
      except pygame.error as e:
          print(f"ошибка зарузки  {filename}: {e}")
          raise
      self.dx = dx
      self.dy = dy

  def move(self):
      self.rect.x += self.dx
      self.rect.y += self.dy

  def bounce(self, screen_width, screen_height):
      if self.rect.left <= 0 or self.rect.right >= screen_width:
          self.dx *= -1
      if self.rect.top <= 0 or self.rect.bottom >= screen_height:
          self.dy *= -1

  def draw(self):
      mw.blit(self.image, (self.rect.x, self.rect.y))