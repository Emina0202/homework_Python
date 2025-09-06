import pytest
import json
import requests


# Фикстура для получения токена авторизации на API Yougile
@pytest.fixture(scope="module")
def get_token():
    auth_data = {
        "login": "emina89637979259@gmail.com",
        "password": "umar/2020/",
        "companyId": "c0b180aa-0d96-4289-9753-c9b08950859f"
    }

    headers = {'Content-Type': 'application/json'}

    # Отправляем POST-запрос на сервер для получения ключа авторизации
    response = requests.post(
        'https://ru.yougile.com/api-v2/auth/keys',
        data=json.dumps(auth_data),
        headers=headers
    )
    token = response.json()['key']
    yield token


# Фикстура для получения списка пользователей
@pytest.fixture(scope="module")
def get_user_list(get_token):
    token = "rL6IrqOzW66+Fwx+68Aqda4X+980EKThSc93vkrjkih6jEUFnrfF2BoI7ejT3Ixo"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Отправляем GET-запрос для получения списка пользователей
    response = requests.get(
        'https://ru.yougile.com/api-v2/users',
        headers=headers
    )
    print(response.json())
    return response.json()


# Тест на создание нового проекта
def test_create_project(get_token):
    project_data = {"title": "новый проект для тестирования"}

    token = "rL6IrqOzW66+Fwx+68Aqda4X+980EKThSc93vkrjkih6jEUFnrfF2BoI7ejT3Ixo"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Отправляем POST-запрос для создания проекта
    response = requests.post(
        'https://ru.yougile.com/api-v2/projects',
        data=json.dumps(project_data),
        headers=headers
    )

    print(response.json())
    assert response.status_code == 201


# Тест на обновление существующего проекта
def test_edit_project(get_token):
    edit_data = {
        "deleted": False,
        "title": "новый проект для тестирования1"
    }

    token = "rL6IrqOzW66+Fwx+68Aqda4X+980EKThSc93vkrjkih6jEUFnrfF2BoI7ejT3Ixo"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Отправляем PUT-запрос для обновления проекта
    response = requests.put(
        'https://ru.yougile.com/api-v2/projects/'
        '805a7cc8-9466-4593-a8d8-5543d4ba1a6c',
        data=json.dumps(edit_data),
        headers=headers
    )

    print(response.json())
    assert response.status_code == 200


# Тест на получение проекта по ID
def test_bind_by_id(get_token):
    auth_data = {"title": "новый проект для тестирования1"}

    token = "rL6IrqOzW66+Fwx+68Aqda4X+980EKThSc93vkrjkih6jEUFnrfF2BoI7ejT3Ixo"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Отправляем GET-запрос для получения проекта
    response = requests.get(
        'https://ru.yougile.com/api-v2/projects/'
        '805a7cc8-9466-4593-a8d8-5543d4ba1a6c',
        headers=headers
    )

    print(response.json())
    assert response.status_code == 200
