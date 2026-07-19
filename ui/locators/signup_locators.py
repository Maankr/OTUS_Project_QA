from selenium.webdriver.common.by import By


class SignupLocators:

    # форма регистрации
    NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    EMAIL_EXISTS_ERROR = (By.XPATH, "//p[contains(text(),'Email Address already exist')]")

    # страница Account Information
    TITLE_MR = (By.ID, "id_gender1")
    TITLE_MRS = (By.ID, "id_gender2")
    PASSWORD = (By.ID, "password")
    DAYS = (By.ID, "days")
    MONTHS = (By.ID, "months")
    YEARS = (By.ID, "years")
    FIRSTNAME = (By.ID, "first_name")
    LASTNAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS = (By.ID, "address1")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE = (By.ID, "mobile_number")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    ACCOUNT_CREATED = (By.XPATH, "//b[text()='Account Created!']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
