from requests import Session, Response


class BaseClient:
    # каждый клиент получает свой URL
    # сессия создается 1 раз, все запрсы идут через нее
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = Session()

    def _build_url(self, endpoint: str) -> str:
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    # возвращает идентификаторы всех бронирований
    def get(self, endpoint: str, **kwargs) -> Response:
        return self.session.get(self._build_url(endpoint), **kwargs)

    # создаёт новый токен аутентификации
    def post(self, endpoint: str, **kwargs) -> Response:
        return self.session.post(self._build_url(endpoint), **kwargs)

    # обновление текущего бронирования
    def put(self, endpoint: str, **kwargs) -> Response:
        return self.session.put(self._build_url(endpoint), **kwargs)

    # частичное обновление объекта
    def patch(self, endpoint: str, **kwargs) -> Response:
        return self.session.patch(self._build_url(endpoint), **kwargs)

    def delete(self, endpoint: str, **kwargs) -> Response:
        return self.session.delete(self._build_url(endpoint), **kwargs)

    def close(self):
        self.session.close()