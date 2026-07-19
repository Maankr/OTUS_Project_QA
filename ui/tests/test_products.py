import allure
import pytest


@allure.feature("Товары")
class TestProducts:

    @allure.story("Навигация")
    @allure.title("Переход в каталог товаров через хедер")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.products
    def test_navigate_to_products_via_header(self, home_page):

        with allure.step("Открываем главную страницу"):
            home_page.open()

        with allure.step("Кликаем 'Products' в хедере"):
            home_page.open_products_page()

        with allure.step("Проверяем, что открылась страница каталога"):
            current_url = home_page.get_current_url()

            allure.attach(
                current_url,
                name="URL после перехода",
                attachment_type=allure.attachment_type.TEXT
            )

            assert "/products" in current_url

    @allure.story("Просмотр каталога товаров")
    @allure.title("Проверка отображения списка товаров")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.products
    def test_products_list(self, products_page):

        with allure.step("Открываем страницу товаров"):

            products_page.open()

            allure.attach(
                products_page.get_current_url(),
                name="URL страницы товаров",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Проверяем, что список товаров загружен"):

            products_count = products_page.get_products_count()

            allure.attach(
                str(products_count),
                name="Количество товаров",
                attachment_type=allure.attachment_type.TEXT
            )

            assert products_count > 0


    @allure.story("Поиск товаров")
    @allure.title("Поиск товара по ключевому слову")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.products
    def test_search_product(self, products_page):

        with allure.step("Открываем страницу товаров"):

            products_page.open()

        with allure.step("Выполняем поиск товара"):

            search_text = "Tshirt"

            allure.attach(
                search_text,
                name="Поисковый запрос",
                attachment_type=allure.attachment_type.TEXT
            )

            products_page.search_product(search_text)

        with allure.step("Проверяем результаты поиска"):

            products_count = products_page.get_products_count()

            allure.attach(
                str(products_count),
                name="Количество найденных товаров",
                attachment_type=allure.attachment_type.TEXT
            )

            assert products_count > 0


    @allure.story("Просмотр товара")
    @allure.title("Открытие страницы товара")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.products
    def test_view_product_details(self, products_page):

        with allure.step("Открываем страницу товаров"):

            products_page.open()

        with allure.step("Открываем первый товар"):

            products_page.open_first_product()

            allure.attach(
                products_page.get_current_url(),
                name="URL страницы товара",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Проверяем отображение информации о товаре"):

            is_open = products_page.is_product_details_open()

            allure.attach(
                str(is_open),
                name="Страница товара открыта",
                attachment_type=allure.attachment_type.TEXT
            )

            assert is_open