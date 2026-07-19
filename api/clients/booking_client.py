from api.clients.base_client import BaseClient
from config.config import API_URL


class BookingClient(BaseClient):
    BOOKING_ENDPOINT = "/booking"

    def __init__(self):
        super().__init__(API_URL)

    def create_booking(self, payload: dict):
        return self.post(self.BOOKING_ENDPOINT, json=payload)

    # получить список всех бронирований
    def get_bookings(self, params: dict = None):
        return self.get(self.BOOKING_ENDPOINT, params=params)

    # получить бронирование по id
    def get_booking(self, booking_id: int):
        return self.get(f"{self.BOOKING_ENDPOINT}/{booking_id}")

    # полное обновление бронирования
    def update_booking(self, booking_id: int, payload: dict, token: str = None):
        return self.put(f"{self.BOOKING_ENDPOINT}/{booking_id}", json=payload, headers=self._auth_header(token))

    # частичное обновление бронирования
    def partial_update_booking(self, booking_id: int, payload: dict, token: str = None):
        return self.patch(f"{self.BOOKING_ENDPOINT}/{booking_id}", json=payload, headers=self._auth_header(token))

    # удалить бронирование
    def delete_booking(self, booking_id: int, token: str = None):
        return self.delete(f"{self.BOOKING_ENDPOINT}/{booking_id}", headers=self._auth_header(token))

    def filter_by_firstname(self, firstname: str):
        return self.get(self.BOOKING_ENDPOINT, params={"firstname": firstname})

    def filter_by_lastname(self, lastname: str):
        return self.get(self.BOOKING_ENDPOINT, params={"lastname": lastname})

    def filter_by_date(self, checkin: str = None, checkout: str = None):
        params = {}

        if checkin:
            params["checkin"] = checkin
        if checkout:
            params["checkout"] = checkout

        return self.get(self.BOOKING_ENDPOINT, params=params)

    def _auth_header(self, token: str = None):
        if not token:
            return {}

        return {"Cookie": f"token={token}"}