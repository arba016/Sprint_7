import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        default=os.getenv("BASE_URL", "https://vitrina.tv/"),
        help="Base URL for the tested site.",
    )
    parser.addoption(
        "--browser",
        choices=("chrome", "firefox"),
        default=os.getenv("BROWSER", "chrome"),
        help="Browser used by Selenium.",
    )
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run browser with a visible UI.",
    )
    parser.addoption(
        "--window-size",
        default=os.getenv("WINDOW_SIZE", "1440,1000"),
        help="Browser window size in WIDTH,HEIGHT format.",
    )
    parser.addoption(
        "--timeout",
        type=int,
        default=int(os.getenv("SELENIUM_TIMEOUT", "10")),
        help="Explicit wait timeout in seconds.",
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture(scope="session")
def timeout(request):
    return request.config.getoption("--timeout")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headed = request.config.getoption("--headed")
    window_size = request.config.getoption("--window-size")
    timeout = request.config.getoption("--timeout")

    if browser == "chrome":
        options = ChromeOptions()
        if not headed:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--window-size={window_size}")
        options.add_argument("--lang=ru-RU")
        options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
        web_driver = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        if not headed:
            options.add_argument("-headless")
        web_driver = webdriver.Firefox(options=options)
        width, height = [int(value) for value in window_size.split(",", maxsplit=1)]
        web_driver.set_window_size(width, height)

    web_driver.set_page_load_timeout(timeout)
    web_driver.implicitly_wait(0)

    yield web_driver

    web_driver.quit()
