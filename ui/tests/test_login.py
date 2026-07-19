import allure
import pytest


@allure.feature("Авторизация")
class TestLogin:

    @allure.story("Успешный вход")
    @allure.title("Логин зарегистрированного пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login
    def test_success_login(
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

        with allure.step("Переходим на страницу логина"):
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

            login_page.wait_until_logged_in()
            
        with allure.step("Проверяем успешную авторизацию"):

            is_logged = login_page.is_logged_in()

            allure.attach(
                str(is_logged),
                name="Статус авторизации",
                attachment_type=allure.attachment_type.TEXT
            )

            assert is_logged


    @allure.story("Негативный сценарий")
    @allure.title("Логин с неверным паролем")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.login
    def test_invalid_login(
            self,
            home_page,
            login_page,
            registered_user
    ):

        with allure.step("Открываем главную страницу"):
            home_page.open()

        with allure.step("Переходим на страницу логина"):
            home_page.open_login_page()

        with allure.step("Вводим корректный email и неверный пароль"):

            allure.attach(
                registered_user["email"],
                name="Email пользователя",
                attachment_type=allure.attachment_type.TEXT
            )

            login_page.login(
                registered_user["email"],
                "wrong_password"
            )

        with allure.step("Проверяем сообщение об ошибке"):

            error_visible = login_page.is_error_visible()

            allure.attach(
                str(error_visible),
                name="Отображение ошибки",
                attachment_type=allure.attachment_type.TEXT
            )

            if error_visible:
                allure.attach(
                    login_page.get_error_message(),
                    name="Текст ошибки",
                    attachment_type=allure.attachment_type.TEXT
                )

            assert error_visible