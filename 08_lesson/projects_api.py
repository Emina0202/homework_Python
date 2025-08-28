import requests
from config import Config


class ProjectsAPI:
    def __init__(self):
        self.base_url = Config.API_URL
        self.headers = {
            "Authorization": f"Bearer {Config.API_TOKEN}",
            "Content-Type": "application/json"
        }

    def create_project(self, project_data):
        """POST /api-v2/projects - создание проекта"""
        url = f"{self.base_url}/projects"
        response = requests.post(url, json=project_data, headers=self.headers)
        return response

    def get_project(self, project_id):
        """GET /api-v2/projects/{id} - получение проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def update_project(self, project_id, update_data):
        """PUT /api-v2/projects/{id} - обновление проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.put(url, json=update_data, headers=self.headers)
        return response

    def delete_project(self, project_id):
        """Дополнительный метод для очистки (если доступен)"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.delete(url, headers=self.headers)
        return response
