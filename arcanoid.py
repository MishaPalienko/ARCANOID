import pygame
pygame.init()

import sys
print(sys.path)

from Area import mw
from Picture import Picture
from moveBall import moveBall


from initialization import game;

#создание монстров и размер их картинки 
for j in range(3):  
    y = game.start_y + (40 * j)
    x = game.start_x + (40 * j)
    for i in range(9 - j):
        d = Picture("./enemy.png", x, y, 40, 40)
        game.monsters.append(d)
        x += 50

# Основной игровой цикл
while not game.game_over:
    mw.fill(game.back)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.gameOver()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.moveRight()
            elif event.key == pygame.K_LEFT:
                game.moveLeft()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                game.stop()
            elif event.key == pygame.K_LEFT:
                game.stop()

    if game.move_right and game.platform.rect.right < 500:
        game.platform.rect.x += game.platform_speed
    if game.move_left and game.platform.rect.left > 0:
        game.platform.rect.x -= game.platform_speed

    # Движение мяча
    for b in game.balls:
        moveBall(b)

    for projectile in game.projectiles[:]:
        projectile.move()

        # Если снаряд касается платформы, конец игры
        if projectile.rect.colliderect(game.platform.rect):
            game.gameOver()
            print("YOU LOSE")
            break

        # Удаление снаряда, если он вышел за экран
        if projectile.rect.top > 500:
            game.projectiles.remove(projectile)  

    # Отображение объектов
    game.platform.draw()
    # Рисуем мячи
    for each_ball in game.balls:
        each_ball.draw()
    
    # Рисуем монстров
    for monster in game.monsters:
        monster.draw()
    
    # Рисуем снаряды
    for projectile in game.projectiles:
        projectile.draw()  # Используем draw() для правильной отрисовки

    pygame.display.update()
    game.clock.tick(30)
