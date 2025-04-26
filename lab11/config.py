from configparser import ConfigParser

def load_config(filename='C:/vscode/labs/.vscode/.vscode/lab11/database.ini', section='postgresql'):
    parser = ConfigParser() # Создаём объект parser, который будет читать .ini файл
    parser.read(filename)# Открываем и читаем содержимое

    config = {}# Создаём пустой словарь , куда будем класть все параметры
    if parser.has_section(section):# Проверяем существует ли секция если секция найдена, получаем все пары (ключ, значение) из этой секции
        params = parser.items(section)
        for param in params: # Вставляем каждый параметр в словарь config
            config[param[0]] = param[1]
    else:# Если указанная секция не найдена, выбрасываем исключение с сообщением об ошибке
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config
#Проверяем: если этот скрипт запущен напрямую
if __name__ == '__main__':
    config = load_config()# Вызываем функцию load_config, и грузим настройки
    print(config)