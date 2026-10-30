# Sprint_7

Автотесты API учебного сервиса «Яндекс Самокат».

## Стек

- Python 3
- requests
- pytest
- allure-pytest
- Allure

## Документация сервиса

- Базовый URL: https://qa-scooter.praktikum-services.ru
- Документация API: https://qa-scooter.praktikum-services.ru/docs/

## Что покрыто тестами

| Эндпоинт | Файл | Проверки |
| --- | --- | --- |
| `POST /api/v1/courier` — создание курьера | `tests/test_create_courier.py` | успешное создание (201, `{"ok": true}`), два одинаковых курьера (409), отсутствие обязательных полей (400), логин уже используется (409) |
| `POST /api/v1/courier/login` — логин курьера | `tests/test_login_courier.py` | успешная авторизация (200, возвращает `id`), отсутствие полей (400/504), неверный пароль и несуществующий пользователь (404) |
| `POST /api/v1/orders` — создание заказа | `tests/test_create_order.py` | параметризация по цветам: только BLACK, только GREY, оба цвета, без цвета (201, возвращает `track`) |
| `GET /api/v1/orders` — список заказов | `tests/test_list_orders.py` | в теле ответа возвращается список заказов (200) |

## Установка и запуск

1. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

2. Запустите тесты:

   ```bash
   pytest tests
   ```

3. Запуск тестов с сохранением результатов Allure:

   ```bash
   pytest tests --alluredir=allure-results
   ```

4. Просмотр отчёта Allure:

   ```bash
   allure serve allure-results
   ```

   или генерация статического отчёта:

   ```bash
   allure generate allure-results -o allure-report --clean
   ```

## Структура проекта

```
Sprint_7/
├── tests/                 # тесты, по отдельному классу на каждую ручку
│   ├── test_create_courier.py
│   ├── test_login_courier.py
│   ├── test_create_order.py
│   └── test_list_orders.py
├── sender_requests.py     # методы отправки HTTP-запросов (с @allure.step)
├── helpers.py             # вспомогательные методы генерации данных и регистрации курьера
├── data.py                # статичные данные: URL и тела запросов
├── conftest.py
├── requirements.txt
├── allure-report/         # сгенерированный отчёт Allure
└── README.md
```

## Примечания

- Тестовые данные создаются перед тестом и удаляются после его выполнения, поэтому все тесты независимы.
- Известная особенность сервиса: при авторизации без пароля API возвращает код 504.
