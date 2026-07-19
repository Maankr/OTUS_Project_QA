import allure
import pytest


@allure.feature("Регистрация")
class TestSignup:

    @allure.story("Создание нового пользователя")
    @allure.title("Успешная регистрация нового пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.signup
    def test_register_new_user(
            self,
            home_page,
            signup_page,
            test_user
    ):

        with allure.step("Открываем главную страницу"):

            home_page.open()

            allure.attach(
                home_page.get_current_url(),
                name="URL главной страницы",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Переходим на страницу регистрации"):

            home_page.open_login_page()

        with allure.step("Заполняем форму регистрации"):

            signup_page.register_user(test_user)

            allure.attach(
                test_user["email"],
                name="Email нового пользователя",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                test_user["name"],
                name="Имя пользователя",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Проверяем успешное создание аккаунта"):

            account_created = signup_page.is_account_created()

            allure.attach(
                str(account_created),
                name="Аккаунт создан",
                attachment_type=allure.attachment_type.TEXT
            )

            assert account_created


    @allure.story("Регистрация с занятым email")
    @allure.title("Повторная регистрация с уже существующим email")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.signup
    @pytest.mark.negative
    def test_signup_with_existing_email(
            self,
            home_page,
            signup_page,
            registered_user
    ):

        with allure.step("Открываем главную страницу"):
            home_page.open()

        with allure.step("Переходим на страницу регистрации"):
            home_page.open_login_page()

        with allure.step("Пробуем зарегистрироваться с уже занятым email"):
            signup_page.start_registration(
                name="Another User",
                email=registered_user["email"]
            )

        with allure.step("Проверяем сообщение об ошибке"):
            assert signup_page.is_email_exists_error_visible()


    @allure.story("Авторизация после регистрации")
    @allure.title("После регистрации пользователь автоматически авторизован")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.signup
    def test_user_logged_after_signup(
            self,
            home_page,
            signup_page,
            login_page,
            test_user
    ):

        with allure.step("Открываем главную страницу"):

            home_page.open()

        with allure.step("Переходим на страницу регистрации"):

            home_page.open_login_page()

        with allure.step("Регистрируем нового пользователя"):

            signup_page.register_user(test_user)

            allure.attach(
                test_user["email"],
                name="Email зарегистрированного пользователя",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Проверяем успешное создание аккаунта"):

            account_created = signup_page.is_account_created()

            allure.attach(
                str(account_created),
                name="Статус создания аккаунта",
                attachment_type=allure.attachment_type.TEXT
            )

            assert account_created

        with allure.step("Нажимаем кнопку Continue"):

            signup_page.click_continue()

        with allure.step("Проверяем автоматическую авторизацию"):

            is_logged = login_page.is_logged_in()

            allure.attach(
                str(is_logged),
                name="Пользователь авторизован",
                attachment_type=allure.attachment_type.TEXT
            )

            assert is_logged