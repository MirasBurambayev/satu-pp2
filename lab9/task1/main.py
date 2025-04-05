# Импорт библиотек
import pygame, sys
from pygame.locals import *
import random, time

# Инициализация Pygame
pygame.init()

# Основные параметры
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

# Создание игрового окна
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("shumaher")

# Цвета
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Шрифты и текст
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Фоновое изображение
background = pygame.image.load(r"C:\vscode\labs\.vscode\.vscode\lab9\task1\AnimatedStreet.png")
display.fill(WHITE)

# Игровой флаг и настройки времени
runn = True
FPS = 60
clock = pygame.time.Clock()

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\vscode\labs\.vscode\.vscode\lab9\task1\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс тенге (даёт 5 очков и ускорение)
class Tenge(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\vscode\labs\.vscode\.vscode\lab9\task1\icons8-тенге-64-removebg-preview.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE, SPEED
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 5
            SPEED += 0.5
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс тенге 2 (даёт 1 очко и небольшое ускорение)
class Tenge2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\vscode\labs\.vscode\.vscode\lab9\task1\icons8-тенге-64_1_-removebg-preview.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE, SPEED
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            SPEED += 0.1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\vscode\labs\.vscode\.vscode\lab9\task1\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# СОЗДАНИЕ объектов (исправление: Tg2 должен быть экземпляром!)
Tg2 = Tenge2()
Tg = Tenge()
P1 = Player()
E1 = Enemy()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(Tg)
all_sprites.add(Tg2)

# Событие для увеличения скорости каждые 1000 мс
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Главный игровой цикл
while runn:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  # Автоматическое ускорение игры
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Фон и счёт
    display.blit(background, (0, 0))
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    display.blit(scores, (10, 10))

    # Движение и отрисовка всех спрайтов
    for entity in all_sprites:
        entity.move()
        display.blit(entity.image, entity.rect)

    # Проверка на столкновение с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        # Экран Game Over
        display.fill(RED)
        display.blit(game_over, (30, 250))
        pygame.display.update()

        # Удаление объектов и завершение игры
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Обновление экрана
    pygame.display.update()
    clock.tick(FPS)
