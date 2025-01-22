from initialization import game
from Bomb import Bomb
from Ball import Ball


platform = game.platform
monsters = game.monsters
projectiles = game.projectiles
max_speed = game.max_speed
monster_counter = game.monster_counter
game_over = game.game_over

def moveBall(b):
    b.rect.x += b.dx
    b.rect.y += b.dy

    
    if b.rect.left <= 0 or b.rect.right >= 500:
        # Этот код разворачивает мяч при ударе об стену
        b.dx *= -1 
    if b.rect.top <= 0:
        b.dy *= -1
        # Этот код разворачивает мяч при ударе о платформу
    if b.rect.colliderect(platform.rect):
        b.dy *= -1

    if b.rect.bottom >= 500:
        # 1. Если мяч улетел то удаляем его из списка
        game.removeBall(b)
        # 2. Если мячей не осталось, то проигрыш
        if len(game.balls) == 0:
          game.gameOver()
          print("YOU LOSE")

    # Проверка столкновений с монстрами
    for monster in monsters[:]:
        if b.rect.colliderect(monster.rect):
            monsters.remove(monster)
            b.dy *= -1

            # Увеличение скорости мяча на 10% (ограничено максимальной скоростью)
            b.dx = max(min(b.dx * 1.6, max_speed), -max_speed)
            b.dy = max(min(b.dy * 1.6, max_speed), -max_speed)

            # тут ты можешь создавать новый мяч и помещать его в список bals
            # ball = Ball("./ball.png", 200, 300, 20, 20, dx, dy)
            # bals.append(ball)
            # Но нужно немного менять траекторию иначе мячи будут двигаться вместе

            # Если это третий монстр, создаем снаряд
            global monster_counter
            monster_counter += 1
            if monster_counter % 35 == 0:  # Если номер монстра делится на 10, то создаем снаряд
                projectile = Bomb(monster.rect.centerx - 5, monster.rect.bottom, width=80, height=80)  # Увеличение размера
                projectiles.append(projectile)
            
            
            if monster_counter % 2 == 0:  # Если номер монстра делится на 10, то создаем снаряд
              game.addBall(Ball("./ball.png", 200, 300, 20, 20, b.dx, b.dy))
              

            break

                










