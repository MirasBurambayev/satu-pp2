import pygame
from pygame.locals import *

pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program Extended")

# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = {
    K_1: ("Red", (255, 0, 0)),       
    K_2: ("Green", (0, 255, 0)),     
    K_3: ("Blue", (0, 0, 255)),      
    K_4: ("Black", (0, 0, 0)),       
    K_5: ("Eraser", (255, 255, 255)) 
}

# Переменные состояния
drawing = False            
start_pos = (0, 0)         
mode = "brush"             
color_name, color = "Black", BLACK  
radius = 5                 

# Шрифт 
font = pygame.font.SysFont("Verdana", 20)

# Заливаем фон 
screen.fill(WHITE)
pygame.display.update()

# Функция отображения подсказок в верхней части экрана
def draw_hint():
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 60))

    # текущий режим и цвет
    line1 = f"Mode: {mode.upper()} | Color: {color_name.upper()}"
    # горячие клавиши
    line2 = "[1]Red [2]Green [3]Blue [4]Black [5]Eraser | [B]Brush [R]Rect [C]Circle"

    # Отрисовываем строки 
    text1 = font.render(line1, True, BLACK)
    text2 = font.render(line2, True, BLACK)
    screen.blit(text1, (10, 5))
    screen.blit(text2, (10, 30))

# Главный цикл
running = True
while running:
    draw_hint()  
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False  

        # начало рисования
        elif event.type == MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            if mode == "brush" or mode == "eraser":
                pygame.draw.circle(screen, color, event.pos, radius)

        # Обработка отпускания мыши — 
        elif event.type == MOUSEBUTTONUP:
            if mode == "rect":
                end_pos = event.pos
                # Создание прямоугольника от 
                rect = pygame.Rect(*start_pos, *(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, color, rect, width=2)
            elif mode == "circle":
                end_pos = event.pos
                # Вычисляем центр и радиус круга
                center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                radius_circle = max(abs(end_pos[0] - start_pos[0]) // 2, abs(end_pos[1] - start_pos[1]) // 2)
                pygame.draw.circle(screen, color, center, radius_circle, width=2)
            drawing = False  

        # Обработка движения мыши во время рисования (кисть/ластик)
        elif event.type == MOUSEMOTION and drawing:
            if mode == "brush" or mode == "eraser":
                pygame.draw.circle(screen, color, event.pos, radius)

        # Обработка нажатия клавиш — выбор цвета или режима
        elif event.type == KEYDOWN:
            if event.key in COLORS:
                # Меняем цвет и автоматически включаем кисть
                color_name, color = COLORS[event.key]
                mode = "eraser" if event.key == K_5 else "brush"
            elif event.key == K_r:
                mode = "rect"
            elif event.key == K_c:
                mode = "circle"
            elif event.key == K_b:
                mode = "brush"

    # Обновление  окна
    pygame.display.update()

pygame.quit()
