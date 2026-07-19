from config.config import UI_URL
from ui.pages.base_page import BasePage
from ui.locators.home_locators import HomeLocators


class HomePage(BasePage):

    def open(self):
        super().open(UI_URL)
        self.close_cookie_popup()

    def open_login_page(self):
        self.click(HomeLocators.SIGNUP_LOGIN_BUTTON)

    def is_home_page_open(self):
        return self.is_visible(HomeLocators.HOME_LOGO)

    def open_products_page(self):
        self.click(HomeLocators.PRODUCTS_BUTTON)