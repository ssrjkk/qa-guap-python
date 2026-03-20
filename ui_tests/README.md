# UI Tests - ГУАП и метро Петербурга

Тестирую сайты, которыми пользуюсь сам:
- **guap.ru** - сайт моего университета
- **metro.spb.ru** - езжу каждый день на учёбу

## Паттерн: Page Object Model

```
ui_tests/
├── conftest.py           # Chrome WebDriver (headless)
├── pages/
│   ├── base_page.py      # Базовый класс: find, click, type_text...
│   ├── guap_page.py      # Страницы сайта ГУАП
│   └── metro_page.py     # Страница сайта метро СПб
└── test_spb_sites.py     # Тест-сьют
```

## Зачем POM?

Если сайт поменяет вёрстку - я правлю локатор в одном месте, а не ищу его по всем тестам.

## Запуск

```bash
pip install selenium webdriver-manager pytest
pytest ui_tests/ -v
```

Нужен установленный Google Chrome.  
`webdriver-manager` сам скачает подходящий ChromeDriver.
