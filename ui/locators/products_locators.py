from selenium.webdriver.common.by import By


class ProductsLocators:

    PRODUCT_LIST = (By.CSS_SELECTOR, ".product-image-wrapper")
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".product-image-wrapper")
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, "button.close-modal")
    VIEW_CART = (By.CSS_SELECTOR, ".modal-content a[href='/view_cart']")
    PRODUCT_DETAILS = (By.CSS_SELECTOR, ".product-information")
    MODAL_WINDOW = (By.CSS_SELECTOR, ".modal-content")
    FIRST_VIEW_PRODUCT = (By.XPATH, "(//a[contains(text(),'View Product')])[1]")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR,"a.add-to-cart")