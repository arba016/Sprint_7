from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.base_page import BasePage


class HomePage(BasePage):
    MAIN_HEADING = (By.XPATH, "//h1[contains(normalize-space(), 'Витрина ТВ')]")
    COOKIE_NOTICE = (
        By.XPATH,
        "//*[contains(normalize-space(), 'обработки cookie-файлов')]",
    )
    COOKIE_ACCEPT_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Согласен'] | //*[@role='button' and normalize-space()='Согласен']",
    )
    PRIVACY_POLICY_LINK = (
        By.XPATH,
        "//a[contains(normalize-space(), 'Политикой конфиденциальности')]",
    )

    def load(self, base_url):
        self.open(base_url)

    def heading_text(self):
        return self.find(self.MAIN_HEADING).text

    def accept_cookies_if_present(self):
        try:
            self.short_wait.until(EC.element_to_be_clickable(self.COOKIE_ACCEPT_BUTTON)).click()
        except TimeoutException:
            return False
        return True

    def privacy_policy_href(self):
        return self.find(self.PRIVACY_POLICY_LINK).get_attribute("href")

    def cookie_notice_is_visible(self):
        return self.is_visible(self.COOKIE_NOTICE)

    def cookie_notice_is_hidden(self):
        try:
            self.short_wait.until(EC.invisibility_of_element_located(self.COOKIE_NOTICE))
        except TimeoutException:
            return False
        return True
