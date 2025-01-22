import pygame
pygame.init()

import sys
print(sys.path)

from Area import mw
from Picture import Picture
from moveBall import moveBall


from initialization import game_state; 

#создание монстров и размер их картинки 
for j in range(3):  
    y = game_state.start_y + (40 * j)
    x = game_state.start_x + (40 * j) // 2
    for i in range(9 - j):
        d = Picture("./enemy.png", x, y, 40, 40)
        game_state.monsters.append(d)
        x += 50

# Основной игровой цикл
while not game_state.game_over:
    mw.fill(game_state.back)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game_state.moveRight()
            elif event.key == pygame.K_LEFT:
                game_state.moveLeft()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                game_state.stop()
            elif event.key == pygame.K_LEFT:
                game_state.stop()

    if game_state.move_right and game_state.platform.rect.right < 500:
        game_state.platform.rect.x += game_state.platform_speed
    if game_state.move_left and game_state.platform.rect.left > 0:
        game_state.platform.rect.x -= game_state.platform_speed

    # Движение мяча
    for b in game_state.balls:
        moveBall(b)

    for projectile in game_state.projectiles[:]:
        projectile.move()

        # Если снаряд касается платформы, конец игры
        if projectile.rect.colliderect(game_state.platform.rect):
            game_over = True
            print("YOU LOSE")
            break

        # Удаление снаряда, если он вышел за экран
        if projectile.rect.top > 500:
            game_state.projectiles.remove(projectile)  

    # Отображение объектов
    game_state.platform.draw()
    # Рисуем мячи
    for each_ball in game_state.balls:
        each_ball.draw()
    
    # Рисуем монстров
    for monster in game_state.monsters:
        monster.draw()
    
    # Рисуем снаряды
    for projectile in game_state.projectiles:
        projectile.draw()  # Используем draw() для правильной отрисовки

    pygame.display.update()
    game_state.clock.tick(30)
