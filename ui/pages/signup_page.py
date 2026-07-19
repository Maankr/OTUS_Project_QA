from selenium.webdriver.support.ui import Select

from ui.pages.base_page import BasePage
from ui.locators.signup_locators import SignupLocators


class SignupPage(BasePage):

    def enter_name(self, name):
        self.type(SignupLocators.NAME_INPUT, name)

    def enter_email(self, email):
        self.type(SignupLocators.EMAIL_INPUT, email)

    def click_signup(self):
        self.click(SignupLocators.SIGNUP_BUTTON)

    def start_registration(self, name, email):
        self.enter_name(name)
        self.enter_email(email)
        self.click_signup()

     # поверить сообщение о том, что email уже занят
    def is_email_exists_error_visible(self):
        return self.is_visible(
            SignupLocators.EMAIL_EXISTS_ERROR
        )

    # заполнение формы Account Information
    def fill_account_information(
        self,
        password,
        birth_day,
        birth_month,
        birth_year,
        firstname,
        lastname,
        company,
        address,
        country,
        state,
        city,
        zipcode,
        mobile
    ):

        self.click(SignupLocators.TITLE_MR)
        self.type(SignupLocators.PASSWORD, password)
        Select(
            self.find(SignupLocators.DAYS)
        ).select_by_visible_text(birth_day)
        Select(
            self.find(SignupLocators.MONTHS)
        ).select_by_visible_text(birth_month)
        Select(
            self.find(SignupLocators.YEARS)
        ).select_by_visible_text(birth_year)
        self.type(SignupLocators.FIRSTNAME, firstname)
        self.type(SignupLocators.LASTNAME, lastname)
        self.type(SignupLocators.COMPANY, company)
        self.type(SignupLocators.ADDRESS, address)
        Select(
            self.find(SignupLocators.COUNTRY)
        ).select_by_visible_text(country)
        self.type(SignupLocators.STATE, state)
        self.type(SignupLocators.CITY, city)
        self.type(SignupLocators.ZIPCODE, zipcode)
        self.type(SignupLocators.MOBILE, mobile)

    def create_account(self):

        self.click(
            SignupLocators.CREATE_ACCOUNT
        )
        self.find(
            SignupLocators.ACCOUNT_CREATED
        )

    def is_account_created(self):
        return self.is_visible(
            SignupLocators.ACCOUNT_CREATED
        )

    def click_continue(self):
        self.click(SignupLocators.CONTINUE_BUTTON)

    def register_user(self, user):
        self.start_registration(
        user["name"],
        user["email"]
    )

        self.fill_account_information(
        password=user["password"],
        birth_day=user["birth_day"],
        birth_month=user["birth_month"],
        birth_year=user["birth_year"],
        firstname=user["firstname"],
        lastname=user["lastname"],
        company=user["company"],
        address=user["address"],
        country=user["country"],
        state=user["state"],
        city=user["city"],
        zipcode=user["zipcode"],
        mobile=user["mobile"]
    )
        
        self.create_account()