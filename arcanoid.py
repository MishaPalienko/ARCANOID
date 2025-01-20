import pygame

pygame.init()

back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Game")

clock = pygame.time.Clock()
max_platform_speed = 30
racket_x = 200
racket_y = 430
dx = 3
dy = 3
max_speed = 10  # Ограничение максимальной скорости
move_right = False
move_left = False
platform_speed = 5
game_over = False
platform = None
ball = None
monsters = []
platform_speed = min(platform_speed * 2.1, max_platform_speed)
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


# Класс для снаряда
class Projectile(Area):
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


class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        super().__init__(x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (width, height))

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


# Инициализация платформы и мяча
platform = Picture("./platform.png", racket_x, racket_y, 100, 20)
ball = Picture("./ball.png", 200, 300, 20, 20)

# Создание монстров
start_x = 5
start_y = 5
for j in range(3):
    y = start_y + (40 * j)
    x = start_x + (40 * j) // 2
    for i in range(9 - j):
        d = Picture("./enemy.png", x, y, 40, 40)
        monsters.append(d)
        x += 50

# Список снарядов
projectiles = []

# Счетчик для проверки каждого 3-го монстра
monster_counter = 0

# Основной игровой цикл
while not game_over:
    mw.fill(back)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_LEFT:
                move_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_LEFT:
                move_left = False

    if move_right and platform.rect.right < 500:
        platform.rect.x += platform_speed
    if move_left and platform.rect.left > 0:
        platform.rect.x -= platform_speed

    # Движение мяча
    ball.rect.x += dx
    ball.rect.y += dy

    if ball.rect.left <= 0 or ball.rect.right >= 500:
        dx *= -1
    if ball.rect.top <= 0:
        dy *= -1

    if ball.rect.colliderect(platform.rect):
        dy *= -1

    if ball.rect.bottom >= 500:
        game_over = True
        print("YOU LOSE")

    # Проверка столкновений с монстрами
    for monster in monsters[:]:
        if ball.rect.colliderect(monster.rect):
            monsters.remove(monster)
            dy *= -1

            # Увеличение скорости мяча на 10% (ограничено максимальной скоростью)
            dx = max(min(dx * 1.6, max_speed), -max_speed)
            dy = max(min(dy * 1.6, max_speed), -max_speed)

            # Если это третий монстр, создаем снаряд
            monster_counter += 1
            if monster_counter % 7 == 0:  # Если номер монстра делится на 3, то создаем снаряд
                projectile = Projectile(monster.rect.centerx - 5, monster.rect.bottom, width=80, height=80)  # Увеличение размера
                projectiles.append(projectile)
            break
        # if monster_counter % 10 == 0:
            # add one more ball
            # ball = False

    for projectile in projectiles[:]:
        projectile.move()

        # Если снаряд касается платформы, конец игры
        if projectile.rect.colliderect(platform.rect):
            game_over = True
            print("YOU LOSE")
            break

        # Удаление снаряда, если он вышел за экран
        if projectile.rect.top > 500:
            projectiles.remove(projectile)

    # Отображение объектов
    platform.draw()
    ball.draw()
    
    # Рисуем монстров
    for monster in monsters:
        monster.draw()
    # Рисуем снаряды
    for projectile in projectiles:
        projectile.draw()  # Используем draw() для правильной отрисовки

    pygame.display.update()
    clock.tick(30)
