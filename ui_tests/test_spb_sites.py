import pytest
from selenium.webdriver.common.by import By
from pages.guap_page import GuapMainPage
from pages.metro_page import SpbMetroPage

class TestGuapMainPage:

    def test_guap_main_page_opens(self, driver):
        page = GuapMainPage(driver)
        page.open_main()

        assert page.get_page_title() != ""

    def test_guap_title_contains_university_name(self, driver):
        page = GuapMainPage(driver)
        page.open_main()
        title = page.get_page_title().lower()

        assert any(word in title for word in ["гуап", "guap", "аэрокосмическ", "университет"])

    def test_guap_url_is_correct(self, driver):
        page = GuapMainPage(driver)
        page.open_main()
        assert "guap.ru" in page.get_current_url()

    def test_guap_header_is_visible(self, driver):
        page = GuapMainPage(driver)
        page.open_main()
        assert page.is_header_visible()

    def test_guap_page_has_content(self, driver):
        page = GuapMainPage(driver)
        page.open_main()
        body = driver.find_element(By.TAG_NAME, "body")
        assert len(body.text) > 100, "Страница выглядит пустой"

class TestSpbMetroPage:

    def test_metro_page_opens(self, driver):
        page = SpbMetroPage(driver)
        page.open()
        assert page.get_page_title() != ""

    def test_metro_url_is_correct(self, driver):
        page = SpbMetroPage(driver)
        page.open()
        assert "metro.spb.ru" in page.get_url()

    def test_metro_title_mentions_metro_or_spb(self, driver):
        page = SpbMetroPage(driver)
        page.open()
        title = page.get_page_title().lower()
        assert any(word in title for word in ["метро", "metro", "петербург", "spb", "санкт"])

    def test_metro_page_has_content(self, driver):
        page = SpbMetroPage(driver)
        page.open()
        body = driver.find_element(By.TAG_NAME, "body")
        assert len(body.text) > 50

    def test_metro_page_is_loaded(self, driver):
        page = SpbMetroPage(driver)
        page.open()
        assert page.is_page_loaded()

class TestGuapVsMetro:

    @pytest.mark.parametrize("url, expected_words", [
        ("https://guap.ru", ["гуап", "guap", "университет", "аэрокосмическ"]),
        ("https://www.metro.spb.ru", ["метро", "metro", "петербург", "spb"]),
    ])
    def test_pages_have_relevant_titles(self, driver, url, expected_words):
        driver.get(url)
        title = driver.title.lower()
        assert any(word in title for word in expected_words), \
            f"Заголовок '{driver.title}' не содержит ни одного из: {expected_words}"

    @pytest.mark.parametrize("url", [
        "https://guap.ru",
        "https://www.metro.spb.ru",
    ])
    def test_pages_return_non_empty_body(self, driver, url):
        driver.get(url)
        body = driver.find_element(By.TAG_NAME, "body")
        assert len(body.text) > 100, f"Страница {url} выглядит пустой"
