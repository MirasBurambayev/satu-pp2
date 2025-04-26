import psycopg2
import csv
from config import load_config

def create_table():
    conn = psycopg2.connect(**load_config())# Подключаемся к базе данных
    cur = conn.cursor()# Создаём курсор
    cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    ''')
    conn.commit()# Сохраняем изменения
    cur.close()# Закрываем курсор
    conn.close()# Закрываем соединение
# Функция для вставки данных в таблицу с консоли
def insert_from_console():
    conn = psycopg2.connect(**load_config())
    cur = conn.cursor()
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    # Выполняем SQL-команду вставки одного пользователя
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
# Функция для вставки данных из CSV-файла
def insert_from_csv(filename=r'C:\vscode\labs\.vscode\.vscode\lab11\insert.csv'):
    conn = psycopg2.connect(**load_config())
    cur = conn.cursor()
    # Открываем CSV-файл на чтение
    with open(filename, newline='') as csvfile:
        # Создаём объект reader для построчного чтения CSV
        reader = csv.reader(csvfile)
        # Проходим по каждой строке файла
        for row in reader:
            cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    cur.close()
    conn.close()
# Функция для обновления телефона пользователя
def update_user():
    conn = psycopg2.connect(**load_config())
    cur = conn.cursor()
    #Запрашиваем у пользователя имя, чей номер хотим изменить
    name = input("Enter name to update: ")
    # Запрашиваем новый номер телефона
    new_phone = input("Enter new phone: ")
    # Выполняем SQL-команду обновления записи
    cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, name))
    conn.commit()
    cur.close()
    conn.close()
# Функция для запроса данных из таблицы
def query_data():
    conn = psycopg2.connect(**load_config())
    cur = conn.cursor()
    # Предлагаем выбрать способ фильтрации данных
    print("Filter by:\n1. Username\n2. Phone\n3. All")
    choice = input("Enter choice: ")
    # В зависимости от выбора строим SQL-запрос
    if choice == '1':
        # Фильтрация по имени
        name = input("Enter name: ")
        cur.execute("SELECT * FROM phonebook WHERE username = %s", (name,))
    elif choice == '2':
        # Фильтрация по телефону
        phone = input("Enter phone: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    else:
        # Без фильтрации, вывод всех записей
        cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
# Функция для удаления записей из таблицы
def delete_entry():
    conn = psycopg2.connect(**load_config())
    cur = conn.cursor()
    # Спрашиваем, по какому полю будем удалять
    print("Delete by:\n1. Username\n2. Phone")
    choice = input("Enter choice: ")
    if choice == '1':
         # Удаление по имени
        name = input("Enter name to delete: ")
        cur.execute("DELETE FROM phonebook WHERE username = %s", (name,))
    else:
        # Удаление по телефону
        phone = input("Enter phone to delete: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_table()
    while True:
        print("\n1. Insert from console\n2. Insert from CSV\n3. Update\n4. Query\n5. Delete\n6. Exit")
        opt = input("Choose option: ")
        if opt == '1':
            insert_from_console()
        elif opt == '2':
            insert_from_csv()
        elif opt == '3':
            update_user()
        elif opt == '4':
            query_data()
        elif opt == '5':
            delete_entry()
        elif opt == '6':
            break
        else:
            print("Invalid option.")