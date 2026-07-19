import allure
import pytest


@allure.feature("Booking")
@allure.story("Создание booking")
class TestBookingCreate:

    @allure.title("Создание бронированяи с валидными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.create
    def test_create_booking(self, booking_client, test_booking):

        with allure.step("Отправляем запрос на создание бронирования"):
            response = booking_client.create_booking(test_booking.model_dump())
            allure.attach(str(response.json()), name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверяем наличие id бронирования в ответе"):
            assert "bookingid" in response.json()


    @allure.title("Создание booking без optional поля")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.create
    def test_create_booking_without_optional(self, booking_client, test_booking):

        data = test_booking.model_dump()
        data["additionalneeds"] = None

        with allure.step("Отправляем запрос без optional поля"):
            response = booking_client.create_booking(data)
            allure.attach(str(response.json()), name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверяем статус код"):
            assert response.status_code == 200


    @allure.title("Создание нескольких бронирований")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.create
    def test_create_booking_multiple(self, booking_client, test_booking):

        with allure.step("Создаем 3 бронирования подряд"):
            for i in range(3):
                response = booking_client.create_booking(test_booking.model_dump())
                allure.attach(str(response.json()), name=f"response_{i}", attachment_type=allure.attachment_type.JSON)
                assert "bookingid" in response.json()


    @allure.title("Проверка данных бронирования")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.create
    def test_create_booking_data_integrity(self, booking_client, test_booking):

        with allure.step("Создаем бронирование"):
            response = booking_client.create_booking(test_booking.model_dump())

        with allure.step("Извлекаем данные из ответа"):
            booking = response.json()["booking"]

        with allure.step("Проверяем firstname"):
            assert booking["firstname"] == test_booking.firstname

        with allure.step("Проверяем lastname"):
            assert booking["lastname"] == test_booking.lastname

        with allure.step("Проверяем totalprice"):
            assert booking["totalprice"] == test_booking.totalprice