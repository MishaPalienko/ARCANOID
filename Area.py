import pygame

mw = pygame.display.set_mode((500, 500))

class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        if self.fill_color:
            pygame.draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)