from selenium.webdriver.common.by import By


class CommonLocators:

    # Кнопка согласия в баннере cookie
    COOKIE_CONSENT = ( By.CSS_SELECTOR, ".fc-cta-consent" )