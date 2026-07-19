from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def login(self, email, password):
        self.type(LoginLocators.LOGIN_EMAIL, email)
        self.type(LoginLocators.LOGIN_PASSWORD, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def wait_until_logged_in(self):
        self.find(LoginLocators.LOGGED_USERNAME)

    def get_error_message(self):
        return self.get_text(LoginLocators.LOGIN_ERROR)

    def is_error_visible(self):
        return self.is_visible(LoginLocators.LOGIN_ERROR)

    def is_logged_in(self):
        return self.is_visible(LoginLocators.LOGGED_USERNAME)

    def logout(self):
        self.click(LoginLocators.LOGOUT_BUTTON)
        self.find(LoginLocators.LOGIN_BUTTON)