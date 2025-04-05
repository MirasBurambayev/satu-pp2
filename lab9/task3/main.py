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

# отображения подсказок
def draw_hint():
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 60))

    line1 = f"Mode: {mode.upper()} | Color: {color_name.upper()}"
    line2 = "[1]Red [2]Green [3]Blue [4]Black [5]Eraser"
    line3 = "[B]Brush [R]Rect [C]Circle [S]Square [T]RightTri [E]EquiTri [H]Rhombus"

    # Отрисовываем строки 
    text1 = font.render(line1, True, BLACK)
    text2 = font.render(line2, True, BLACK)
    text3 = font.render(line3, True, BLACK)
    screen.blit(text1, (10, 5))
    screen.blit(text2, (10, 30))
    screen.blit(text3, (10, 55))

# Главный цикл
running = True
while running:
    draw_hint()  
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False 

        #начало рисования
        elif event.type == MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            if mode == "brush" or mode == "eraser":
                pygame.draw.circle(screen, color, event.pos, radius)

        # завершение фигуры
        elif event.type == MOUSEBUTTONUP:
            end_pos = event.pos
            x1, y1 = start_pos
            x2, y2 = end_pos

            if mode == "rect":
                # Прямоугольник
                pygame.draw.rect(screen, color, pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 2)

            elif mode == "square":
                # Квадрат со стороной по меньшему измерению
                side = min(abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen, color, pygame.Rect(x1, y1, side, side), 2)

            elif mode == "circle":
                # Круг по центру и радиусу
                center = ((x1 + x2) // 2, (y1 + y2) // 2)
                radius_circle = max(abs(x2 - x1) // 2, abs(y2 - y1) // 2)
                pygame.draw.circle(screen, color, center, radius_circle, 2)

            elif mode == "right_triangle":
                # Прямоугольный треугольник
                triangle = [start_pos, (x1, y2), (x2, y2)]
                pygame.draw.polygon(screen, color, triangle, 2)

            elif mode == "equilateral":
                # Равносторонний треугольник
                side = abs(x2 - x1)
                height = int(side * (3**0.5) / 2)
                triangle = [start_pos, (x1 + side, y1), (x1 + side // 2, y1 - height)]
                pygame.draw.polygon(screen, color, triangle, 2)

            elif mode == "rhombus":
                # Ромб с центром между точками
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                dx = abs(x2 - x1) // 2
                dy = abs(y2 - y1) // 2
                points = [
                    (center_x, center_y - dy),  
                    (center_x + dx, center_y),  
                    (center_x, center_y + dy), 
                    (center_x - dx, center_y)   
                ]
                pygame.draw.polygon(screen, color, points, 2)

            drawing = False  # Завершение рисования

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
            elif event.key == K_s:
                mode = "square"
            elif event.key == K_t:
                mode = "right_triangle"
            elif event.key == K_e:
                mode = "equilateral"
            elif event.key == K_h:
                mode = "rhombus"

    # Обновление окна
    pygame.display.update()

pygame.quit()
