# Guap.ru Framework (Python)

Portfolio Project

Фреймворк для автоматизации тестирования веб-приложения guap.ru.

---

## Зачем этот проект

Автоматизирует проверку ключевых сценариев образовательного портала ГУАП:

| Сценарий | Тип теста | Зачем |
|----------|-----------|-------|
| Авторизация студента | UI + API | Проверка входа и сессии |
| Просмотр расписания | API + DB | Валидация данных: фронт <-> бэк <-> БД |
| Проверка личных данных | API | Контроль целостности профиля |
| Нагрузка на эндпоинты | k6 | Оценка деградации при росте запросов |

---

## Быстрый старт

```bash
# Клонировать
git clone https://github.com/ssrjkk/guap-test-framework-python.git
cd guap-test-framework-python

# Установить зависимости
pip install -r requirements.txt

# Запустить тесты
pytest api_tests -v          # API-тесты
pytest ui_tests -v           # UI-тесты (требуется браузер)
pytest -m smoke              # Smoke-тесты

# Сгенерировать отчёт
pytest --alluredir=allure-results
allure serve allure-results
```

---

## Архитектура

```
.
├── api_client/                 # HTTP-клиент с retry, логированием, таймаутами
│   ├── base.py                 # BaseApiClient
│   ├── clients.py              # Эндпоинты: GuapApiClient
│   └── schemas.py              # Валидация схем ответов
├── api_tests/                  # API-тесты
│   ├── conftest.py             # Фикстуры: api_client, http_session
│   └── test_api_clients.py
├── ui_tests/                   # UI-тесты (Selenium)
│   ├── conftest.py             # Фикстуры: driver, page, wait
│   ├── pages/                  # Page Objects
│   │   ├── base_page.py
│   │   ├── guap_page.py
│   │   └── metro_page.py
│   └── test_pages.py
├── load_tests/                 # k6-скрипты для нагрузочного тестирования
│   ├── api_basic.js
│   └── api_crud.js
├── sql_tasks/                  # SQL-запросы для валидации данных
│   └── guap_db_queries.sql 
├── tests_data/                 # Тестовые данные и factories
│   └── factories.py
├── config/                     # Конфигурация из .env
│   └── settings.py
├── conftest.py                 # Глобальные фикстуры
└── .github/workflows/          # CI/CD
    └── ci.yml
```

---

## Пример теста

```python
# api_tests/test_api_clients.py
def test_api_student_by_id(api_client):
    """GET /api/students/:id - получение студента по ID"""
    response = api_client.get("/api/students/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data or "student_id" in data
```

```python
# ui_tests/pages/guap_page.py
class GuapMainPage(BasePage):
    def open_main(self):
        self.open("https://guap.ru")
    
    def is_header_visible(self):
        return self.is_visible(self.HEADER)
```

---

## Стек

| Технология | Зачем |
|------------|-------|
| `pytest` | Оркестрация, фикстуры, маркеры `@smoke`, `@regression` |
| `requests` | HTTP-клиент с retry и логированием |
| `Selenium` | UI-автоматизация с Page Objects |
| `k6` | Нагрузочное тестирование |
| `Docker` | Воспроизводимое окружение |
| `GitHub Actions` | CI/CD: lint -> tests -> report |

---

## Запуск в Docker

```bash
docker build -t qa-tests .
docker run --rm qa-tests pytest api_tests -v
docker run --rm qa-tests pytest ui_tests -v
```

---

## CI/CD

GitHub Actions автоматически запускает:
1. **lint** - flake8 проверка стиля
2. **api-tests** - API тесты
3. **ui-tests** - UI тесты (с автоскриншотами при падениях)

---

## Качество кода

```bash
# Проверка стиля
flake8 . --max-line-length=120

# Все тесты
pytest -v

# По тегам
pytest -m smoke
pytest -m regression
pytest -m critical
```

---

## Контакты

- Telegram: @ssrjkk
- Email: ray013lefe@gmail.com
