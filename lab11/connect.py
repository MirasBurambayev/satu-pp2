import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """# Пытаемся подключиться к серверу PostgreSQL с использованием переданных параметров
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn # Возвращаем  подключения для следующих работ
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    config = load_config()
    connect(config)