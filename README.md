# Frontend-тестирование на основе веб-приложения AutomationExercise и Backend-тестирование на основе API Restful-Booker

Учебный проект по автоматизации тестирования: покрытие автотестами публичного интернет-магазина [AutomationExercise](https://automationexercise.com/) (UI) и публичного API [Restful Booker](https://restful-booker.herokuapp.com/apidoc/index.html) (API).

## Цель

Систематизировать и применить на практике знания, полученные на курсе.

## Что покрыто

- **UI** — 12 тестов: регистрация, вход/выход, каталог и поиск товаров, корзина. Подробнее в [`ui/README.md`](ui/README.md).
- **API** — 25 тестов: авторизация, CRUD по бронированиям, фильтрация, негативные сценарии. Подробнее в [`api/README.md`](api/README.md).

```

## CI — Jenkins

В корне лежит `Jenkinsfile` — пайплайн с этапами: checkout → установка зависимостей → запуск API-тестов → сборка Allure-отчёта прямо в Jenkins.
`Jenkins/Dockerfile` — образ Jenkins с добавленным Python, Chrome и Firefox для запуска тестов внутри контейнера.
```