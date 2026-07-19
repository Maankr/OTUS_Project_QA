import allure
import pytest


@allure.feature("Smoke")
@allure.story("Проверка доступности API")
class TestSmoke:

    @allure.title("Проверка доступности сервиса")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_ping(self, booking_client):

        with allure.step("Пингуем сервис"):
            response = booking_client.get("/ping")
            allure.attach(str(response.status_code), name="status_code")

        with allure.step("Проверяем доступность сервиса"):
            assert response.status_code == 201

    @allure.title("Получение списка бронирований")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_get_bookings(self, booking_client):

        with allure.step("Отправляем запрос на получение списка бронирований"):
            response = booking_client.get_bookings()
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверяем успешный статус ответа"):
            assert response.status_code == 200

        with allure.step("Проверяем, что ответ является списком"):
            assert isinstance(response.json(), list)

    @allure.title("Проверка авторизации")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_auth_basic(self, auth_client):

        with allure.step("Отправляем запрос на получение токена"):
            response = auth_client.authenticate()
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверяем успешную авторизацию"):
            assert response.status_code == 200

        with allure.step("Проверяем наличие токена"):
            assert "token" in response.json()