from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.base_page import BasePage


class HomePage(BasePage):
    MAIN_HEADING = (By.XPATH, "//h1[contains(normalize-space(), 'Витрина ТВ')]")
    META_DESCRIPTION = (By.CSS_SELECTOR, "meta[name='description']")
    COOKIE_NOTICE = (
        By.XPATH,
        "//*[contains(normalize-space(), 'обработки cookie-файлов')]",
    )
    COOKIE_ACCEPT_BUTTON = (By.ID, "accept-agreements-button")
    PRIVACY_POLICY_LINK = (
        By.XPATH,
        "//a[contains(normalize-space(), 'Политикой конфиденциальности')]",
    )
    COMPANY_LINK = (By.XPATH, "//a[normalize-space()='О компании']")
    CONTACTS_LINK = (By.XPATH, "//a[normalize-space()='Контакты']")
    SCHEDULE_FALLBACK = (
        By.XPATH,
        "//*[contains(normalize-space(), 'Расписание телеканала')]",
    )

    def load(self, base_url):
        self.open(base_url)

    def heading_text(self):
        return self.find_present(self.MAIN_HEADING).get_attribute("textContent").strip()

    def meta_description(self):
        return self.find_present(self.META_DESCRIPTION).get_attribute("content")

    def accept_cookies_if_present(self):
        try:
            self.short_wait.until(EC.element_to_be_clickable(self.COOKIE_ACCEPT_BUTTON)).click()
        except TimeoutException:
            return False
        return True

    def privacy_policy_href(self):
        return self.find(self.PRIVACY_POLICY_LINK).get_attribute("href")

    def accepted_agreements_cookie(self):
        return self.driver.get_cookie("accept_agreements")

    def cookie_notice_is_visible(self):
        return self.is_visible(self.COOKIE_NOTICE)

    def cookie_notice_is_hidden(self):
        try:
            self.short_wait.until(EC.invisibility_of_element_located(self.COOKIE_NOTICE))
        except TimeoutException:
            return False
        return True

    def reload(self):
        self.driver.refresh()
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    def company_href(self):
        return self.find(self.COMPANY_LINK).get_attribute("href")

    def contacts_href(self):
        return self.find(self.CONTACTS_LINK).get_attribute("href")

    def schedule_fallback_text(self):
        return self.find_present(self.SCHEDULE_FALLBACK).get_attribute("textContent")
