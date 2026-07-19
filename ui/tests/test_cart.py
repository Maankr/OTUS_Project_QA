import allure
import pytest


@allure.feature("Корзина")
class TestCart:

    @allure.story("Добавление товара")
    @allure.title("Добавление товара в корзину")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.cart
    def test_add_product_to_cart(
            self,
            products_page,
            cart_page
    ):

        with allure.step("Открываем страницу товаров"):
            products_page.open()

        with allure.step("Добавляем первый товар в корзину"):
            products_page.add_first_product_to_cart()

        with allure.step("Переходим в корзину"):
            products_page.open_cart()

        with allure.step("Проверяем количество товаров в корзине"):
            count = cart_page.get_cart_items_count()

            allure.attach(
                str(count),
                name="Количество товаров",
                attachment_type=allure.attachment_type.TEXT
            )

            assert count == 1

    @allure.story("Удаление товара")
    @allure.title("Удаление товара из корзины")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.cart
    def test_remove_product_from_cart(
            self,
            products_page,
            cart_page
    ):

        with allure.step("Открываем страницу товаров"):
            products_page.open()

        with allure.step("Добавляем первый товар в корзину"):
            products_page.add_first_product_to_cart()

        with allure.step("Переходим в корзину"):
            products_page.open_cart()

        with allure.step("Удаляем товар из корзины"):
            cart_page.remove_first_item()

        with allure.step("Проверяем, что корзина пуста"):
            is_empty = cart_page.is_cart_empty()

            allure.attach(
                str(is_empty),
                name="Корзина пуста",
                attachment_type=allure.attachment_type.TEXT
            )

            assert is_empty