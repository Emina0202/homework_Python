import pytest
from config import Config


@pytest.fixture
def auth_headers():
    """Фикстура для авторизационных заголовков"""
    return {
        "Authorization": f"Bearer {Config.TOKEN}",
        "Content-Type": "application/json"
    }


@pytest.fixture
def base_url():
    """Фикстура для базового URL"""
    return Config.API_URL


@pytest.fixture
def test_project_data():
    """Фикстура с тестовыми данными проекта"""
    return {
        "title": "Test Project",
        "description": "Test project description"
    }
