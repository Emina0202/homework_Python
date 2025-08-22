import pytest
from projects_api import ProjectsAPI


class TestProjectsAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api = ProjectsAPI()
        self.created_projects = []

    def teardown_method(self):
        """Очистка созданных проектов после каждого теста"""
        for project_id in self.created_projects:
            self.api.delete_project(project_id)

    # POSITIVE TESTS

    def test_create_project_positive(self, test_project_data):
        """Позитивный тест создания проекта"""
        response = self.api.create_project(test_project_data)

        assert response.status_code == 201
        assert "id" in response.json()
        assert response.json()["title"] == test_project_data["title"]

        project_id = response.json()["id"]
        self.created_projects.append(project_id)

    def test_get_project_positive(self, test_project_data):
        """Позитивный тест получения проекта"""
        # Сначала создаем проект
        create_response = self.api.create_project(test_project_data)
        project_id = create_response.json()["id"]
        self.created_projects.append(project_id)

        # Получаем проект
        get_response = self.api.get_project(project_id)

        assert get_response.status_code == 200
        assert get_response.json()["id"] == project_id
        assert get_response.json()["title"] == test_project_data["title"]

    def test_update_project_positive(self, test_project_data):
        """Позитивный тест обновления проекта"""
        # Сначала создаем проект
        create_response = self.api.create_project(test_project_data)
        project_id = create_response.json()["id"]
        self.created_projects.append(project_id)

        # Обновляем проект
        update_data = {
            "title": "Updated Project Title",
            "description": "Updated description"
        }
        update_response = self.api.update_project(project_id, update_data)

        assert update_response.status_code == 200
        assert update_response.json()["title"] == update_data["title"]

        # Проверяем, что изменения сохранились
        get_response = self.api.get_project(project_id)
        assert get_response.json()["title"] == update_data["title"]

    # NEGATIVE TESTS

    def test_create_project_negative_missing_title(self):
        """Негативный тест создания проекта без обязательного поля title"""
        invalid_data = {
            "description": "Project without title"
        }

        response = self.api.create_project(invalid_data)

        assert response.status_code == 400
        # Проверяем, что проект не был создан
        assert "id" not in response.json()

    def test_get_project_negative_not_found(self):
        """Негативный тест получения несуществующего проекта"""
        non_existent_id = "non-existent-id-12345"

        response = self.api.get_project(non_existent_id)

        assert response.status_code == 404

    def test_update_project_negative_invalid_data(self):
        """Негативный тест обновления проекта с невалидными данными"""
        # Сначала создаем валидный проект
        create_response = self.api.create_project({
            "title": "Test Project",
            "description": "Test description"
        })
        project_id = create_response.json()["id"]
        self.created_projects.append(project_id)

        # Пытаемся обновить с невалидными данными
        invalid_data = {
            "title": ""  # Пустой title недопустим
        }

        response = self.api.update_project(project_id, invalid_data)

        # Ожидаем ошибку валидации
        assert response.status_code in [400, 422]

    def test_update_project_negative_not_found(self):
        """Негативный тест обновления несуществующего проекта"""
        non_existent_id = "non-existent-id-12345"
        update_data = {
            "title": "Updated Title"
        }

        response = self.api.update_project(non_existent_id, update_data)

        assert response.status_code == 404
