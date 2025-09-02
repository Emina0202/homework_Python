import pytest
import json
import requests


# Фикстура для получения токена авторизации на API Yougile
@pytest.fixture(scope="module")
def get_token():
    auth_data = {
        "login": "emina89637979259@gmail.com",
        "password": "umar/2020/",
        "companyId": "9347006b-dc75-4550-97d5-3008ba00d4a0"  # ID компании
    }

    headers = {'Content-Type': 'application/json'}  # Заголовки HTTP-запроса

# Отправляем POST-запрос на сервер для получения ключа авторизации
    response = requests.post(
        'https://ru.yougile.com/api-v2/auth/keys',
        data=json.dumps(auth_data),  # Преобразование данных в JSON
        headers=headers              # Передача заголовков
    )
    token = response.json()['key']
    yield token


 # Фикстура для получения списка пользователей


@pytest.fixture(scope="module")
def get_user_list(get_token):
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer LMO2a+0uZ5mfMmU2wUFLvOx3Lmckd77jrKVc6AvNs1PUOlc5JNzeG12ysmwur7aj'  # Заголовки с токеном
               }                                       # авторизации

# Отправляем GET-запрос для получения списка пользователей
    response = requests.get(
        'https://ru.yougile.com/api-v2/users',
        headers=headers
    )
    print(response.json())  # Печать полученного ответа (для дебага)
    # return response.json()  # Возврат списка пользователей
    get_user_list(
        'LMO2a+0uZ5mfMmU2wUFLvOx3Lmckd77jrKVc6AvNs1PUOlc5JNzeG12ysmwur7aj')


# Тест на создание нового проекта
def test_create_project(get_token):
    project_data = {
  "title": "ГосУслуги",
  "users": {
    "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
    "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
  }
}

# Заголовки с токеном авторизации
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer LMO2a+0uZ5mfMmU2wUFLvOx3Lmckd77jrKVc6AvNs1PUOlc5JNzeG12ysmwur7aj'}

# Отправляем POST-запрос для создания проекта
    response = requests.post(
        'https://ru.yougile.com/api-v2/projects',
        data=json.dumps(project_data),  # Данные проекта в виде JSON
        headers=headers                 # Заголовки запроса
    )
    # Печать результата операции (для дебага)
    print(response.json())

    # Утверждение успешного статуса ответа (ожидаем 201 Created)
    assert response.status_code == 201

# Тест на обновление существующего проекта
def test_edit_project(get_token):
    edit_data = {
        "deleted": False,              # Проект не удалён
        "title": "ГосУслуги1",         # Новое название проекта
        "users": {
    "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
    "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
  }
    }
    # Заголовки с токеном авторизации
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer LMO2a+0uZ5mfMmU2wUFLvOx3Lmckd77jrKVc6AvNs1PUOlc5JNzeG12ysmwur7aj'}

    # Отправляем PUT-запрос для обновления проекта
    response = requests.put(
        'https://ru.yougile.com/api-v2/projects/'
        '003400df-16f3-4452-83f9-f5e03d48f5cd',
        data=json.dumps(edit_data),     # Обновленные данные проекта
        headers=headers                 # Заголовки запроса
    )
    # Печать результата операции (для дебага)
    print(response.json())

    # Утверждение успешного статуса ответа (ожидаем 200 OK)
    assert response.status_code == 200


# Тест на связывание проекта с пользователями
def test_bind_by_id(get_token):
    auth_data = {
        "title": "ГосУслуги1",  # Название проекта
        "users": {
    "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
    "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
  }
    }
    # Заголовки с токеном авторизации
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer LMO2a+0uZ5mfMmU2wUFLvOx3Lmckd77jrKVc6AvNs1PUOlc5JNzeG12ysmwur7aj'}
    # Отправляем POST-запрос для связывания проекта с пользователями
    response = requests.get(
        'https://ru.yougile.com/api-v2/projects/'
        '003400df-16f3-4452-83f9-f5e03d48f5cd',
        data=json.dumps(auth_data),             # Данные проекта
        headers=headers                         # Заголовки запроса

    )
    # Печать результата операции (для дебага)
    print(response.json())

    # Утверждение успешного статуса ответа (ожидаем 201 Created)

    assert response.status_code == 200


def test_delete_project(get_token):
    project_data = {
        "title": "ГосУслуги",  # Название проекта
        "users": {
    "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
    "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
  }
    }

# Заголовки с токеном авторизации
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer LMO2a+0uZ5mfMmU2wUFLvOx3Lmckd77jrKVc6AvNs1PUOlc5JNzeG12ysmwur7aj'}

# Отправляем POST-запрос для создания проекта
    response = requests.post(
        'https://ru.yougile.com/api-v2/auth/keys/{key}',
        data=json.dumps(project_data),  # Данные проекта в виде JSON
        headers=headers                 # Заголовки запроса
    )
    # Печать результата операции (для дебага)
    print(response.json())

    # Утверждение успешного статуса ответа (ожидаем 201 Created)
    assert response.status_code == 200
