from ui.pages.base_page import BasePage
from ui.locators.products_locators import ProductsLocators

from config.config import UI_URL


class ProductsPage(BasePage):

    URL = f"{UI_URL}/products"

    def open(self):
        super().open(self.URL)
        self.close_cookie_popup()

    def get_products_count(self):
        return len(self.find_all(ProductsLocators.PRODUCT_LIST))

    def search_product(self, product_name):
        self.type(ProductsLocators.SEARCH_INPUT, product_name)
        self.click(ProductsLocators.SEARCH_BUTTON)

    def open_first_product(self):
        self.click(ProductsLocators.FIRST_VIEW_PRODUCT)

    def is_product_details_open(self):
        return self.is_visible(ProductsLocators.PRODUCT_DETAILS)

    def add_first_product_to_cart(self):
        product = self.find(ProductsLocators.FIRST_PRODUCT)
        self.scroll_to(ProductsLocators.FIRST_PRODUCT)
        self.hover(ProductsLocators.FIRST_PRODUCT)
        button = product.find_element(*ProductsLocators.ADD_TO_CART_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)
        self.find(ProductsLocators.MODAL_WINDOW)

    def continue_shopping(self):
        self.click(ProductsLocators.CONTINUE_SHOPPING)

    def open_cart(self):
        self.click(ProductsLocators.VIEW_CART)
        self.wait.until(lambda driver: "view_cart" in driver.current_url)