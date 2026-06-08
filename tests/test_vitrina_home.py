from tests.pages.home_page import HomePage


def test_homepage_loads_and_contains_expected_identity(driver, base_url, timeout):
    home_page = HomePage(driver, timeout)

    home_page.load(base_url)
    home_page.accept_cookies_if_present()

    assert "Витрина ТВ" in driver.title
    assert "Витрина ТВ" in home_page.heading_text()
    assert home_page.text_is_visible("смотреть прямой эфир")


def test_cookie_notice_links_to_privacy_policy_and_can_be_accepted(driver, base_url, timeout):
    home_page = HomePage(driver, timeout)

    home_page.load(base_url)

    assert home_page.cookie_notice_is_visible()
    assert home_page.privacy_policy_href().startswith("https://")

    assert home_page.accept_cookies_if_present()
    assert home_page.cookie_notice_is_hidden()


def test_schedule_section_is_visible_on_homepage(driver, base_url, timeout):
    home_page = HomePage(driver, timeout)

    home_page.load(base_url)
    home_page.accept_cookies_if_present()

    assert home_page.text_is_visible("Расписание телеканала")


def test_homepage_main_content_is_visible_on_mobile_viewport(driver, base_url, timeout):
    home_page = HomePage(driver, timeout)
    driver.set_window_size(390, 844)

    home_page.load(base_url)
    home_page.accept_cookies_if_present()

    assert "Витрина ТВ" in home_page.heading_text()
    assert home_page.text_is_visible("смотреть прямой эфир")
