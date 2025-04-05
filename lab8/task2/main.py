import pygame , time ,random
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
pygame.display.set_caption('snake')

# Настройки
clock = pygame.time.Clock()
snake_block = 10
start_speed = 10

# Шрифты
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# вывода счёта и уровня
def show_info(score, level):
    value = score_font.render(f"Счёт: {score}  Уровень: {level}", True, yellow)
    dis.blit(value, [10, 10])

# отрисовка змейки
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

    # Старт
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    level = 1
    speed = start_speed

    # Генерация еды
    def spawn_food():
        while True:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            if [foodx, foody] not in snake_List:
                return foodx, foody

    foodx, foody = spawn_food()

    while not game_over:

        # Обработка события после проигрыша
        while game_close:
            dis.fill(blue)
            message("Вы проиграли! Q - выход | C - заново", red)
            show_info(Length_of_snake - 1, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        # Обработка нажатий клавиш
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

        # Проверка выхода за границы
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка на столкновение с собой
        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        # Отрисовка объектов
        draw_snake(snake_block, snake_List)
        show_info(Length_of_snake - 1, level)
        pygame.display.update()

        # Проверка поедания еды
        if x1 == foodx and y1 == foody:
            foodx, foody = spawn_food()
            Length_of_snake += 1

            # Уровни: каждые 3 еды
            if (Length_of_snake - 1) % 3 == 0:
                level += 1
                speed += 2  # Увеличение скорости

        clock.tick(speed)

    pygame.quit()
    quit()

# Запуск игры
gameLoop()
