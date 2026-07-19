import allure
import pytest


@allure.feature("Booking")
class TestBookingRead:

    @allure.title("Получение существующего бронирования по идентификатору")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.read
    def test_get_booking(self, booking_client, created_booking):

        with allure.step("Отправляем запрос на получение бронирования"):
            response = booking_client.get_booking(created_booking)
            allure.attach(str(response.json()), name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверяем успешный статус ответа"):
            assert response.status_code == 200

        with allure.step("Проверяем, что идентификатор booking корректный"):
            assert response.json()["firstname"] is not None


    @allure.title("Получение несуществующего бронирования")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.read
    def test_get_nonexistent_booking(self, booking_client):

        with allure.step("Отправляем запрос с несуществующим идентификатором"):
            response = booking_client.get_booking(99999999)
            allure.attach(str(response.status_code), name="status_code")
            allure.attach(response.text, name="response")

        with allure.step("Проверяем, что API вернул статус 404"):
            assert response.status_code == 404


    @allure.title("Получение списка всех бронирований")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.read
    def test_get_all_bookings(self, booking_client):

        with allure.step("Отправляем запрос на получение списка бронирований"):
            response = booking_client.get_bookings()
            allure.attach(str(response.json()), name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверяем успешный статус ответа"):
            assert response.status_code == 200

        with allure.step("Проверяем, что ответ является списком"):
            assert isinstance(response.json(), list)

        with allure.step("Проверяем, что список бронирований не пустой"):
            assert len(response.json()) > 0