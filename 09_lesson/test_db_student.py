import pytest
from sqlalchemy import create_engine, inspect, text

# Строка подключения
CONN_STR = "postgresql://postgres:1994@localhost:5432/postgres"

db_engine = create_engine(CONN_STR)


@pytest.fixture(scope="function")
def connection():
    """
    Получаем новое открытое соединение к базе данных для каждого теста.
    Закрываем соединение после завершения теста.
    """
    conn = db_engine.connect()
    yield conn
    conn.close()


@pytest.fixture(scope="function", autouse=True)
def cleanup_test_data(connection):
    """Автоматическая очистка тестовых данных после каждого теста."""
    yield
    # Удаляем все тестовые записи
    connection.execute(text(
        "DELETE FROM student WHERE user_id IN (1000, 2000, 3000)"
    ))
    connection.commit()


def test_can_connect(connection):
    """Проверка, что подключение к БД успешно и есть нужная таблица."""
    inspector = inspect(db_engine)
    table_list = inspector.get_table_names()
    assert 'student' in table_list


def test_add_record(connection):
    """Тест на добавление новой записи."""
    new_user_id = 1000

    # Готовим запрос с параметрами
    insert_query = text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
    """)

    # Выполняем запрос с заданными параметрами
    connection.execute(insert_query, {
        "user_id": new_user_id,
        "level": "Elementary",
        "education_form": "Personal",
        "subject_id": 5
    })
    connection.commit()

    # Проверяем наличие новой записи
    select_query = text("SELECT * FROM student WHERE user_id = :user_id")
    row = connection.execute(select_query, {"user_id": new_user_id}).fetchone()
    assert row is not None, "Запись не была добавлена!"
    assert row[1] == "Elementary"  # Проверяем уровень


def test_modify_record(connection):
    """Тест на обновление существующей записи."""
    updated_level = "Intermediate"
    update_user_id = 2000

    # Добавляем новую запись перед обновлением
    insert_query = text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
    """)
    connection.execute(insert_query, {
        "user_id": update_user_id,
        "level": "Beginner",
        "education_form": "Group",
        "subject_id": 10
    })
    connection.commit()

    # Обновляем уровень студента
    update_query = text("""
        UPDATE student SET level = :new_level WHERE user_id = :user_id
    """)
    connection.execute(update_query, {
        "new_level": updated_level,
        "user_id": update_user_id
    })
    connection.commit()

    # Проверяем обновление уровня
    select_query = text("SELECT level FROM student WHERE user_id = :user_id")
    result = connection.execute(
        select_query, {"user_id": update_user_id}
    ).fetchone()[0]
    assert result == updated_level, "Обновление уровня прошло неудачно."


def test_remove_record(connection):
    """Тест на удаление записи."""
    remove_user_id = 3000

    # Добавляем запись для удаления
    insert_query = text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
    """)
    connection.execute(insert_query, {
        "user_id": remove_user_id,
        "level": "Advanced",
        "education_form": "Corporate",
        "subject_id": 15
    })
    connection.commit()

    # Удаляем запись
    delete_query = text("DELETE FROM student WHERE user_id = :user_id")
    connection.execute(delete_query, {"user_id": remove_user_id})
    connection.commit()

    # Проверяем отсутствие удалённой записи
    select_query = text("SELECT COUNT(*) FROM student WHERE user_id = :user_id")
    count = connection.execute(
        select_query, {"user_id": remove_user_id}
    ).scalar()
    assert count == 0, "Удаление записи не сработало."


if __name__ == "__main__":
    # Для запуска без pytest
    pytest.main([__file__, "-v"])