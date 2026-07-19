from api.clients.base_client import BaseClient
from config.config import API_URL


class AuthClient(BaseClient):
    AUTH_ENDPOINT = "/auth"

    def __init__(self):
        super().__init__(API_URL)

    def authenticate(self, username: str = "admin", password: str = "password123"):
        return self.post(self.AUTH_ENDPOINT, json={"username": username, "password": password})

    def get_token(self, username: str = "admin", password: str = "password123") -> str:
        response = self.authenticate(username, password)
        return response.json().get("token")