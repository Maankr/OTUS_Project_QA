import pytest
import allure


@allure.feature("Booking")
class TestBookingDelete:

    @allure.title("Удаление существующего бронирования")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.delete
    def test_delete_booking(self, booking_client, created_booking, auth_headers):

        with allure.step("Отправляем запрос на удаление booking"):
            response = booking_client.delete_booking(created_booking, token=auth_headers["Cookie"].split("=")[1])
            allure.attach(str(response.status_code), name="status_code")

        with allure.step("Проверяем успешное удаление"):
            assert response.status_code == 201


    @allure.title("Удаление несуществующего booking")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.delete
    def test_delete_nonexistent(self, booking_client, auth_headers):

        with allure.step("Пытаемся удалить несуществующее бронирование"):
            response = booking_client.delete_booking(99999999, token=auth_headers["Cookie"].split("=")[1])
            allure.attach(str(response.status_code), name="status_code")

        with allure.step("Проверяем допустимый статус ответа"):
            assert response.status_code in [201, 405]


    @allure.title("Повторное удаление бронирования")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.delete
    def test_double_delete(self, booking_client, created_booking, auth_headers):

        with allure.step("Первое удаление booking"):
            booking_client.delete_booking(created_booking, token=auth_headers["Cookie"].split("=")[1])

        with allure.step("Повторное удаление того же booking"):
            response = booking_client.delete_booking(created_booking, token=auth_headers["Cookie"].split("=")[1])
            allure.attach(str(response.status_code), name="second_delete_status")

        with allure.step("Проверяем корректный ответ API"):
            assert response.status_code in [404, 405]