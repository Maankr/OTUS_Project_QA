import allure
import pytest


@allure.feature("Booking")
@allure.story("Негативные сценарии")
class TestBookingNegative:

    @allure.title("Создание бронирований с некорректной датой")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    def test_invalid_dates(self, booking_client, test_booking):

        data = test_booking.model_dump()
        data["bookingdates"]["checkout"] = "invalid-date"

        with allure.step("Отправляем запрос с некорректным форматом даты"):
            response = booking_client.create_booking(data)
            allure.attach(str(data), name="request", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверяем, что API обработал некорректные данные"):
            assert response.status_code in [200, 400]


    @allure.title("Создание бронирования без обязательных полей")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.negative
    def test_missing_fields(self, booking_client):

        with allure.step("Отправляем запрос с пустым телом"):
            response = booking_client.create_booking({})
            allure.attach("{}", name="request", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверяем, что API вернул ошибку"):
            assert response.status_code in [400, 500]


    @allure.title("Получение бронирования по несуществующему идентификатору")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    def test_get_wrong_id(self, booking_client):

        with allure.step("Отправляем запрос с некорректным идентификатором booking"):
            response = booking_client.get_booking(-1)
            allure.attach(str(response.status_code), name="status_code")
            allure.attach(response.text, name="response")

        with allure.step("Проверяем, что API вернул ожидаемый статус"):
            assert response.status_code in [404, 400]