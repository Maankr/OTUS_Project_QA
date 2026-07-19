import random
import uuid

import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from ui.pages.cart_page import CartPage
from ui.pages.home_page import HomePage
from ui.pages.login_page import LoginPage
from ui.pages.product_page import ProductsPage
from ui.pages.signup_page import SignupPage


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser for tests: chrome or firefox"
    )

# браузер   
@pytest.fixture
def driver(request):

    browser = request.config.getoption("--browser")


    if browser == "chrome":

        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(
            service=ChromeService(),
            options=options
        )


    elif browser == "firefox":

        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        options.add_argument( "--headless")

        driver = webdriver.Firefox(
            service=FirefoxService(),
            options=options
        )

    else:

        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit() 


# страницы
@pytest.fixture
def home_page(driver):
    return HomePage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def signup_page(driver):
    return SignupPage(driver)


@pytest.fixture
def products_page(driver):
    return ProductsPage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


# тестовые данные
@pytest.fixture
def test_user():

    return {
        "name": f"test{random.randint(1000,9999)}",
        "email": f"test_{uuid.uuid4().hex}@mail.com",
        "password": "Test12345",
        "birth_day": "10",
        "birth_month": "May",
        "birth_year": "1995",
        "firstname": "Мария",
        "lastname": "Крючкова",
        "company": "QA",
        "address": "Street 1",
        "country": "Israel",
        "state": "ON",
        "city": "Hevron",
        "zipcode": "12345",
        "mobile": "1234567890"
    }


# зарегистрированный пользователь
@pytest.fixture
def registered_user(
        home_page,
        signup_page,
        login_page,
        test_user
):

    home_page.open()
    home_page.open_login_page()
    signup_page.register_user(test_user)
    assert signup_page.is_account_created(), "User registration failed"
    signup_page.click_continue()

    # после регистрации выходим,
    # чтобы тест логина начинался с чистого состояния
    login_page.logout()
    return test_user

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when in ("setup", "call") and report.failed:
        driver = item.funcargs.get("driver")

        if driver is not None:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )