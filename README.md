# Sprint_7

Автотесты для сайта [vitrina.tv](https://vitrina.tv/) на Python, pytest и Selenium.

## Что проверяется

- главная страница открывается и содержит ожидаемый заголовок;
- SEO-заголовок и meta description содержат ключевой текст;
- cookie-баннер отображает ссылку на политику конфиденциальности и после согласия сохраняет cookie;
- footer-навигация ведет на страницы `О компании` и `Контакты`;
- fallback-блок расписания телеканала присутствует в DOM;
- footer-навигация доступна в мобильном размере окна.

## Установка

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Для запуска нужен установленный Chrome или Firefox. Selenium Manager автоматически подберет подходящий драйвер.

## Запуск тестов

```bash
pytest
```

Полезные параметры:

```bash
pytest --base-url=https://vitrina.tv/ --browser=chrome
pytest --browser=firefox
pytest --headed
pytest --window-size=390,844
```

Также базовый URL можно задать через переменную окружения:

```bash
BASE_URL=https://vitrina.tv/ pytest
```
