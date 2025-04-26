import pygame, time, random
pygame.init()

# Цвета
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Размеры экрана
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake with Timed Food and Weights')

# Настройки
clock = pygame.time.Clock()
snake_block = 10
start_speed = 10

# Шрифты
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Показ счёта и уровня
def show_info(score, level):
    value = score_font.render(f"Счёт: {score}  Уровень: {level}", True, yellow)
    dis.blit(value, [10, 10])

# Отрисовка змейки
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Сообщение при проигрыше
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Главный цикл
def gameLoop():
    game_over = False
    game_close = False

    # Стартовая позиция
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    level = 1
    speed = start_speed
    score = 0

    # Переменные еды
    foodx = 0
    foody = 0
    food_weight = 1
    food_timer = 0
    food_lifetime = 100  # в тиках (примерно 5 секунд при 60 FPS)

    # Генерация еды с весом и таймером
    def spawn_food():
        fx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        fy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        weight = random.choice([1, 2, 3])  # Вес еды (1, 2 или 3 очка)
        return fx, fy, weight

    foodx, foody, food_weight = spawn_food()
    food_timer = food_lifetime
    #основной цикл
    while not game_over:

        while game_close:
            dis.fill(blue)
            message("Вы проиграли! Q - выход | C - заново", red)
            show_info(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Проверка на выход за границы
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # Рисуем еду 
        food_color = green if food_weight == 1 else (255, 204, 0) if food_weight == 2 else red
        pygame.draw.rect(dis, food_color, [foodx, foody, snake_block, snake_block])

        # Таймер еды
        food_timer -= 1
        if food_timer <= 0:
            foodx, foody, food_weight = spawn_food()
            food_timer = food_lifetime

        # Обновляем змейку
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Столкновение с собой
        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        # Отрисовка
        draw_snake(snake_block, snake_List)
        show_info(score, level)
        pygame.display.update()

        # Съедание еды
        if x1 == foodx and y1 == foody:
            score += food_weight
            Length_of_snake += food_weight
            foodx, foody, food_weight = spawn_food()
            food_timer = food_lifetime

            # Повышение уровня(solo leveling)
            if score // 5 + 1 > level:
                level += 1
                speed += 223

        clock.tick(speed)

    pygame.quit()
    quit()

# Запуск игры
gameLoop()
