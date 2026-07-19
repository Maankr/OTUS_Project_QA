# API-тесты (Restful Booker)

Автотесты для публичного API [Restful Booker](https://restful-booker.herokuapp.com/apidoc/index.html) — сервис бронирования номеров, используется как учебная песочница для API-тестирования.

## Что тут проверяется

- авторизация (получение токена, невалидные/пустые данные);
- CRUD по бронированиям (create / read / update / delete);
- фильтрация бронирований по параметрам;
- негативные сценарии (несуществующий id, невалидные данные, отсутствие обязательных полей).

Тесты помечены маркерами (`pytest.ini`), чтобы можно было гонять их выборочно:

| `smoke` | быстрые проверки, что API живо |
| `auth` | авторизация |
| `create` / `read` / `update` / `delete` | CRUD по бронированиям |
| `negative` | негативные сценарии |
| `filters` | фильтрация |

## Запуск

Из корня проекта:

```bash
pytest api/tests
```

По маркеру:

```bash
pytest -m smoke
pytest -m create
```

## Allure

Тесты снабжены `@allure.title`, `@allure.feature/story`, `allure.step` и `allure.attach`.

```bash
pytest api/tests --alluredir=allure-results
allure serve allure-results
```

## Структура

```
api/
├── clients/        # HTTP-клиенты (base / auth / booking)
├── models/         # pydantic-модели запросов и ответов
├── tests/          # сами тесты
└── conftest.py     # фикстуры: клиенты, токен, тестовые данные
```