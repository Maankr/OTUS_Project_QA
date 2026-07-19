import allure
import pytest


@allure.feature("Авторизация")
class TestLogout:

    @allure.story("Выход из системы")
    @allure.title("Успешный logout зарегистрированного пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.logout
    def test_logout(
            self,
            home_page,
            login_page,
            registered_user
    ):

        with allure.step("Открываем главную страницу"):

            home_page.open()

            allure.attach(
                home_page.get_current_url(),
                name="URL главной страницы",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Переходим на страницу авторизации"):

            home_page.open_login_page()

        with allure.step("Выполняем вход зарегистрированного пользователя"):

            allure.attach(
                registered_user["email"],
                name="Email пользователя",
                attachment_type=allure.attachment_type.TEXT
            )

            login_page.login(
                registered_user["email"],
                registered_user["password"]
            )

        with allure.step("Проверяем успешную авторизацию перед выходом"):

            is_logged = login_page.is_logged_in()

            allure.attach(
                str(is_logged),
                name="Статус авторизации",
                attachment_type=allure.attachment_type.TEXT
            )

            assert is_logged

        with allure.step("Выполняем выход из системы"):

            login_page.logout()

        with allure.step("Проверяем возврат на главную страницу"):

            is_home_open = home_page.is_home_page_open()

            allure.attach(
                str(is_home_open),
                name="Главная страница доступна",
                attachment_type=allure.attachment_type.TEXT
            )

            assert is_home_open