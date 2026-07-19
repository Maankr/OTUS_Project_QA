# UI-тесты (AutomationExercise)

Автотесты для публичного сайта [AutomationExercise](https://automationexercise.com/) — учебный интернет-магазин,  используемый для тренировки автотестов.

## Что тут проверяется

- регистрация нового пользователя;
- вход и выход из системы, включая невалидные данные;
- каталог товаров — отображение списка, поиск, просмотр карточки товара;
- корзина — добавление и удаление товара.

## Как устроено

**Локаторы** (`ui/locators/`) — по одному файлу на страницу (`home_locators.py`, `login_locators.py` и т.д.), плюс `common_locators.py` для элементов, общих для нескольких страниц (например, баннер согласия на cookie).

**Страницы** (`ui/pages/`) — классы PageObject, каждый наследуется от `BasePage`. 

## Браузер

Тесты умеют работать и с Chrome, и с Firefox — выбор через параметр командной строки:

```bash
pytest ui/tests --browser chrome    # по умолчанию
pytest ui/tests --browser firefox
```

## Маркеры

| Маркер | Что помечает |
|---|---|
| `login` | вход в систему |
| `logout` | выход из системы |
| `signup` | регистрация нового пользователя |
| `products` | каталог и поиск товаров |
| `cart` | корзина |

## Запуск

Из корня проекта:

```bash
pytest ui/tests
```

По маркеру:

```bash
pytest -m signup
pytest -m cart
```

## Allure

Тесты снабжены `@allure.title`, `@allure.feature/story`, `allure.step` и `allure.attach`

```bash
pytest ui/tests --alluredir=allure-results
allure serve allure-results
```

### Скриншот при падении

При падении любого UI-теста в `ui/conftest.py` срабатывает хук `pytest_runtest_makereport`, который делает скриншот текущего состояния браузера и прикладывает его к отчёту Allure. 

## Структура

```
ui/
├── locators/       # локаторы: по файлу на страницу + common_locators.py
├── pages/          # PageObject-классы (наследуются от base_page.py)
├── tests/          # сами теьты
└── conftest.py     # фикстуры: driver (chrome/firefox), страницы, тестовый пользователь, создание скриншота.
```