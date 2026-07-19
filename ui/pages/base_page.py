from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

from ui.locators.common_locators import CommonLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.actions = ActionChains(driver)

    def open(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_js(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text


    def is_visible(self, locator):
        try:
            return self.find(locator).is_displayed()
        except TimeoutException:
            return False

    def is_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0


    def scroll_to(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def hover(self, locator):
        element = self.find(locator)
        self.actions.move_to_element(element).perform()

    def wait_until_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    # Закрыть баннер согласия на cookie, если он появился
    def close_cookie_popup(self):
        try:
            button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(CommonLocators.COOKIE_CONSENT)
            )
            button.click()
        except TimeoutException:
            pass