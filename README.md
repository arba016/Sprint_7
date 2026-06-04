# Sprint_7

Проект с автотестами API сервиса «Яндекс Самокат».

В проекте проверяются ручки:

создание курьера;
логин курьера;
создание заказа;
получение списка заказов.

Установка проекта

Клонировать репозиторий:

git clone <ссылка_на_репозиторий>

Перейти в папку проекта:

cd Sprint_7_dev

Создать виртуальное окружение:

python -m venv .venv

Активировать виртуальное окружение.

Для Windows PowerShell:

.\.venv\Scripts\Activate.ps1

Для macOS/Linux:

source venv/bin/activate

Установить зависимости:

pip install -r requirements.txt
Как обновить requirements.txt

Если в проект были добавлены новые пакеты, обновить файл зависимостей можно командой:

pip freeze > requirements.txt

Запуск тестов

Запустить все тесты:

pytest

Запустить тесты с генерацией данных для Allure-отчёта:

pytest --alluredir=allure_results

Просмотр Allure-отчёта

Открыть Allure-отчёт:

allure serve allure_results
Очистка прошлых результатов Allure

Для Windows PowerShell:

Remove-Item -Recurse -Force allure_results

Для macOS/Linux:

rm -rf allure_results
