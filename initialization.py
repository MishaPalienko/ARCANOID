import pygame
from Ball import Ball
from Picture import Picture


class GameState:
    def __init__(self):
        self.monsters = []
        self.monster_counter = 0
        self.racket_x = 200
        self.racket_y = 430
        self.platform = Picture("./platform.png", 200, 430, 100, 20)
        self.max_speed = 15
        self.move_right = False
        self.move_left = False
        self.game_over = False
        self.platform_speed = 15
        self.projectiles = []
        self.balls = [Ball("./ball.png", 200, 300, 20, 20, 3, 3)]
        self.start_x = 5
        self.start_y = 5
        self.clock = pygame.time.Clock()
        self.back = (200, 255, 255)
    
    def gameOver(self):
        self.game_over = True
        self.platform_speed = 0

    def moveRight(self):
        self.move_right = True
        self.move_left = False
    def moveLeft(self):
        self.move_left = True
        self.move_right = False
    def stop(self):
        self.move_right = False
        self.move_left = False
    def addBall(self, ball):
        self.balls.append(ball)
    def removeBall(self, ball):
        self.balls.remove(ball)

  
pygame.display.set_caption("Game")


game = GameState()