-- Создание таблицы
DROP TABLE IF EXISTS user_score;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS phonebook;

CREATE TABLE phonebook (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL
);

-- 1. Функция поиска по шаблону
CREATE OR REPLACE FUNCTION search_by_pattern(p_pattern TEXT)
RETURNS TABLE(id INT, username TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    WHERE username ILIKE '%' || p_pattern || '%'
       OR phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 2. Процедура: вставка одного пользователя с обновлением
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_username TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = p_username) THEN
        UPDATE phonebook SET phone = p_phone WHERE username = p_username;
    ELSE
        INSERT INTO phonebook(username, phone) VALUES (p_username, p_phone);
    END IF;
END;
$$;

-- 3. Массовая вставка пользователей
CREATE OR REPLACE PROCEDURE bulk_insert_users(p_usernames TEXT[], p_phones TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1 .. array_length(p_usernames, 1) LOOP
        IF p_phones[i] ~ '^87[0-9]{9}$' THEN
            CALL insert_or_update_user(p_usernames[i], p_phones[i]);
        ELSE
            RAISE NOTICE 'Некорректный номер: % для пользователя %', p_phones[i], p_usernames[i];
        END IF;
    END LOOP;
END;
$$;

-- 4. Функция с пагинацией
CREATE OR REPLACE FUNCTION get_users_by_page(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, username TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook ORDER BY id LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

-- 5. Удаление по имени или номеру
CREATE OR REPLACE PROCEDURE delete_user(p_value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook WHERE username = p_value OR phone = p_value;
END;
$$;