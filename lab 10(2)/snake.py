# snake.py — полностью исправленная версия Snake с сохранением в PostgreSQL

import pygame, time, random, psycopg2
from config import load_config

# Инициализация Pygame
pygame.init()

# Цвета
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Экран
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake with DB Save')

# Настройки
clock = pygame.time.Clock()
snake_block = 10
start_speed = 10

# Шрифты
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Отображение счёта и уровня
def show_info(score, level):
    value = score_font.render(f"Счёт: {score}  Уровень: {level}", True, yellow)
    dis.blit(value, [10, 10])

# Рисование змейки
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Сообщение при проигрыше
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Получение ID пользователя или создание
def get_or_create_user(username):
    conn = psycopg2.connect(**load_config()) # Подключение к базе
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))# Проверяем, есть ли такой пользователь
    user = cur.fetchone()
    if user:
        user_id = user[0] # Если найден — берём его id
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))  # Иначе добавляем нового
        user_id = cur.fetchone()[0]
        conn.commit() # Сохраняем изменения в БД
    cur.close()
    conn.close()
    return user_id

# Получение прогресса
def get_user_progress(user_id):
    conn = psycopg2.connect(**load_config())
    cur = conn.cursor()
    cur.execute("SELECT level, score FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,)) 
    result = cur.fetchone()# Берём последние данные по уровню и счёту
    cur.close()
    conn.close()
    return result if result else (1, 0) # Если нет записей — возвращаем уровень 1, счёт 0

# Сохранение прогресса
def save_progress(user_id, level, score):
    print(f"СОХРАНЯЕМ: user_id={user_id}, level={level}, score={score}")  # отладка
    conn = psycopg2.connect(**load_config())
    cur = conn.cursor()
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
    conn.commit()
    cur.close()
    conn.close()

# Главный игровой цикл
def gameLoop():
    username = input("Введите имя пользователя: ")# Запрашиваем имя игрока
    user_id = get_or_create_user(username)# Ищем или создаём пользователя
    level, score = get_user_progress(user_id)# Загружаем прогресс
    # Стартовые координаты головы змеи
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = score + 1 # Длина зависит от счёта
    speed = start_speed + (level - 1) * 2  # Скорость увеличивается с каждым уровнем

    # Настройки еды
    foodx = 0
    foody = 0
    food_weight = 1
    food_timer = 0
    food_lifetime = 100
     # Функция генерации еды
    def spawn_food():
        fx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        fy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        weight = random.choice([1, 2, 3])
        return fx, fy, weight

    foodx, foody, food_weight = spawn_food()
    food_timer = food_lifetime
    game_over = False
    game_close = False

    while not game_over:

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(user_id, level, score)
                pygame.quit()
                quit()
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
                elif event.key == pygame.K_q:
                    save_progress(user_id, level, score)
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    save_progress(user_id, level, score)
                    gameLoop()
                elif event.key == pygame.K_p:
                    save_progress(user_id, level, score)
                    game_close = True
        # Проверка выхода змеи за границы окна
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        # Обновляем координаты змеи
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        food_color = green if food_weight == 1 else (255, 204, 0) if food_weight == 2 else red
        pygame.draw.rect(dis, food_color, [foodx, foody, snake_block, snake_block])
        # Обновление таймера еды
        food_timer -= 1
        if food_timer <= 0:
            foodx, foody, food_weight = spawn_food()
            food_timer = food_lifetime
        # Движение змеи
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        # Проверка столкновения головы с телом
        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        draw_snake(snake_block, snake_List)
        show_info(score, level)
        pygame.display.update()
         # Проверка на съедание еды
        if x1 == foodx and y1 == foody:
            score += food_weight
            Length_of_snake += food_weight
            foodx, foody, food_weight = spawn_food()
            food_timer = food_lifetime
            if score // 5 + 1 > level:
                level += 1
                speed += 2

        # экстренный выход на экран проигрыша
        while game_close:
            dis.fill(blue)
            message("Вы проиграли! Q - выход | C - заново", red)
            show_info(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    save_progress(user_id, level, score)
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        save_progress(user_id, level, score)
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        save_progress(user_id, level, score)
                        gameLoop()

        clock.tick(speed)

    pygame.quit()
    quit()

# Запуск
if __name__ == '__main__':
    gameLoop()