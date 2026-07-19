from selenium.webdriver.common.by import By

class HomeLocators:

    SIGNUP_LOGIN_BUTTON = (By.XPATH,"//a[contains(text(),'Signup / Login')]")
    PRODUCTS_BUTTON = ( By.XPATH, "//a[contains(text(),'Products')]")
    CART_BUTTON = ( By.XPATH,"//a[contains(text(),'Cart')]")
    CONTACT_US_BUTTON = ( By.XPATH,"//a[contains(text(),'Contact us')]")
    HOME_LOGO = (By.CSS_SELECTOR, "img[alt='Website for automation practice']")