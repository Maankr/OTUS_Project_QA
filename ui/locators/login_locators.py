from selenium.webdriver.common.by import By


class LoginLocators:

    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGIN_ERROR = (By.XPATH, "//p[contains(text(),'incorrect')]")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    LOGGED_USERNAME = (By.XPATH, "//a[contains(.,'Logged in as')]")