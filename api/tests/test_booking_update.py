import allure
import pytest


@allure.feature("Booking")
@allure.story("Обновление бронирований")
class TestBookingUpdate:

    @allure.title("Полное обновление существующего бронировани")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.update
    def test_update_booking(self, booking_client, created_booking, auth_headers, test_booking):

        data = test_booking.model_dump()
        data["firstname"] = "Updated"

        with allure.step("Отправляем запрос на полное обновление бронирования"):
            response = booking_client.update_booking(created_booking, data, token=auth_headers["Cookie"].split("=")[1])
            allure.attach(str(data), name="request", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверяем успешное обновление booking"):
            assert response.status_code == 200

        with allure.step("Проверяем обновленное имя"):
            assert response.json()["firstname"] == "Updated"


    @allure.title("Частичное обновление booking")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.update
    def test_partial_update(self, booking_client, created_booking, auth_headers):

        payload = {"firstname": "Maria"}

        with allure.step("Отправляем запрос на частичное обновление бронирования"):
            response = booking_client.partial_update_booking(created_booking, payload, token=auth_headers["Cookie"].split("=")[1])
            allure.attach(str(payload), name="request", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверяем успешное частичное обновление"):
            assert response.status_code == 200

        with allure.step("Проверяем обновленное имя"):
            assert response.json()["firstname"] == "Maria"

    @allure.title("Обновление booking без авторизации")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.update
    def test_update_without_token(self, booking_client, created_booking, test_booking):

        with allure.step("Отправляем запрос без токена авторизации"):
            response = booking_client.update_booking(created_booking, test_booking.model_dump(), token=None)
            allure.attach(response.text, name="response")

        with allure.step("Проверяем отказ в доступе"):
            assert response.status_code in [403, 405]

    @allure.title("Проверка сохранения обновленных данных")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.update
    def test_update_check_data(self, booking_client, created_booking, auth_headers, test_booking):

        data = test_booking.model_dump()
        data["firstname"] = "Marla"

        with allure.step("Обновляем данные booking"):
            response = booking_client.update_booking(created_booking, data, token=auth_headers["Cookie"].split("=")[1])
            allure.attach(str(data), name="request", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверяем успешное обновление"):
            assert response.status_code == 200

        with allure.step("Проверяем сохранение новых данных"):
            assert response.json()["firstname"] == "Marla"