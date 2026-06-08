from tests.pages.home_page import HomePage


def test_homepage_loads_with_expected_title_and_seo_metadata(driver, base_url, timeout):
    home_page = HomePage(driver, timeout)

    home_page.load(base_url)
    home_page.accept_cookies_if_present()

    assert "Витрина ТВ" in driver.title
    assert "смотреть прямой эфир" in driver.title
    assert "Витрина ТВ" in home_page.heading_text()
    assert "смотреть прямой эфир" in home_page.meta_description()


def test_cookie_notice_links_to_privacy_policy_and_can_be_accepted(driver, base_url, timeout):
    home_page = HomePage(driver, timeout)

    home_page.load(base_url)

    assert home_page.cookie_notice_is_visible()
    assert home_page.privacy_policy_href() == "https://vitrina.tv/docs/policy.html"

    assert home_page.accept_cookies_if_present()
    assert home_page.accepted_agreements_cookie() is not None

    home_page.reload()

    assert home_page.cookie_notice_is_hidden()


def test_footer_navigation_links_are_visible(driver, base_url, timeout):
    home_page = HomePage(driver, timeout)

    home_page.load(base_url)
    home_page.accept_cookies_if_present()

    assert home_page.company_href() == "https://vitrina.tv/company.html"
    assert home_page.contacts_href() == "https://vitrina.tv/company.html#contacts"


def test_schedule_fallback_exists_in_page_dom(driver, base_url, timeout):
    home_page = HomePage(driver, timeout)

    home_page.load(base_url)
    home_page.accept_cookies_if_present()

    fallback_text = home_page.schedule_fallback_text()

    assert "Расписание телеканала" in fallback_text
    assert "временно недоступно" in fallback_text


def test_footer_navigation_is_visible_on_mobile_viewport(driver, base_url, timeout):
    home_page = HomePage(driver, timeout)
    driver.set_window_size(390, 844)

    home_page.load(base_url)
    home_page.accept_cookies_if_present()

    assert home_page.text_is_visible("О компании")
    assert home_page.text_is_visible("Контакты")
