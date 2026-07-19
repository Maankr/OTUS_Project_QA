from config.config import UI_URL
from ui.pages.base_page import BasePage
from ui.locators.cart_locators import CartLocators


class CartPage(BasePage):

    URL = f"{UI_URL}/view_cart"

    def open(self):
        super().open(self.URL)
        self.close_cookie_popup()

    def get_cart_items(self):
        return self.wait.until(lambda driver: driver.find_elements(*CartLocators.CART_ITEMS))

    def get_cart_items_count(self):
        return len(self.get_cart_items())

    def remove_first_item(self):
        self.click_js(CartLocators.DELETE_BUTTON)
        self.wait.until(lambda driver: len(driver.find_elements(*CartLocators.CART_EMPTY_MESSAGE)) > 0)

    def is_cart_empty(self):
        return self.is_visible(CartLocators.CART_EMPTY_MESSAGE)