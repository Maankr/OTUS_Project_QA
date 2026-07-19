from selenium.webdriver.common.by import By


class CartLocators:

    CART_ITEMS = (By.CSS_SELECTOR, "#cart_info_table tbody tr")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".cart_quantity_delete")
    CART_TABLE = (By.ID, "cart_info_table")
    CART_EMPTY_MESSAGE = (By.XPATH,"//b[contains(text(),'Cart is empty')]")