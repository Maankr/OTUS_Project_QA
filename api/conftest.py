import pytest

from api.clients.auth_client import AuthClient
from api.clients.booking_client import BookingClient
from api.models.booking_models import BookingRequest, BookingDates


# клиенты
@pytest.fixture
def auth_client():
    return AuthClient()

@pytest.fixture
def booking_client():
    return BookingClient()

# токен
@pytest.fixture
def token(auth_client):
    response = auth_client.authenticate()
    return response.json().get("token")

@pytest.fixture
def auth_headers(token):
    return {"Cookie": f"token={token}"}

# тестовые данные
@pytest.fixture
def test_booking():
    return BookingRequest(
        firstname="Мария",
        lastname="Крючкова",
        totalprice=230,
        depositpaid=True,
        bookingdates=BookingDates(checkin="2026-11-10", checkout="2026-16-10"),
        additionalneeds="Breakfast"
    )

@pytest.fixture
def created_booking(booking_client, test_booking, auth_headers):
    response = booking_client.create_booking(test_booking.model_dump())
    booking_id = response.json()["bookingid"]

    yield booking_id

    booking_client.delete_booking(booking_id, token=auth_headers["Cookie"].split("=")[1])