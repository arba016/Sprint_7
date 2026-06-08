from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def xpath_literal(value):
    if "'" not in value:
        return f"'{value}'"
    if '"' not in value:
        return f'"{value}"'

    parts = value.split("'")
    return "concat(" + ', "\'", '.join(f"'{part}'" for part in parts) + ")"


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.short_wait = WebDriverWait(driver, 3)

    def open(self, url):
        self.driver.get(url)
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def is_visible(self, locator):
        try:
            self.short_wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def text_is_visible(self, text):
        locator = ("xpath", f"//*[contains(normalize-space(), {xpath_literal(text)})]")
        return self.is_visible(locator)
