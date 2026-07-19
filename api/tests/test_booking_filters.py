import allure
import pytest


@allure.feature("Booking")
@allure.story("Фильтрация бронирований")
class TestBookingFilters:

    @allure.title("Поиск бронирования по имени")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.filters
    def test_filter_by_firstname(self, booking_client):

        with allure.step("Отправляем запрос на поиск booking по имени"):
            response = booking_client.filter_by_firstname("Мария")
            allure.attach(str(response.json()), name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверяем успешный ответ сервера"):
            assert response.status_code == 200

        with allure.step("Проверяем, что ответ содержит список брониоований"):
            assert isinstance(response.json(), list)

    @allure.title("Поиск бронирований по фамилии")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.filters
    def test_filter_by_lastname(self, booking_client):

        with allure.step("Отправляем запрос на поиск booking по фамилии"):
            response = booking_client.filter_by_lastname("Крючкова")
            allure.attach(str(response.json()), name="response", attachment_type=allure.attachment_type.JSON)

        with allure.step("Проверяем успешный ответ сервера"):
            assert response.status_code == 200

        with allure.step("Проверяем, что ответ содержит список бронирований"):
            assert isinstance(response.json(), list)