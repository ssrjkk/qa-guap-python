from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class GuapMainPage(BasePage):
    URL = "https://guap.ru"

    LOGO = (By.CSS_SELECTOR, ".logo, a[href='/'], img[alt*='ГУАП'], img[alt*='GUAP']")
    SEARCH_ICON = (By.CSS_SELECTOR, "[class*='search'], button[aria-label*='поиск']")
    NAVIGATION = (By.CSS_SELECTOR, "nav, .nav, .menu, header ul")
    HEADER = (By.TAG_NAME, "header")

    def open_main(self):
        self.open(self.URL)

    def is_header_visible(self) -> bool:
        return self.is_visible(self.HEADER)

    def get_page_title(self) -> str:
        return self.get_title()

    def get_current_url(self) -> str:
        return self.get_url()

class GuapSearchPage(BasePage):
    URL = "https://guap.ru/search"

    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='search'], input[name='q'], input[placeholder*='оиск']")
    RESULTS = (By.CSS_SELECTOR, ".search-result, .results, article, .result-item")

    def open_search(self):
        self.open(self.URL)

    def search(self, query: str):
        self.type_text(self.SEARCH_INPUT, query)
        self.find(self.SEARCH_INPUT).send_keys(Keys.ENTER)

    def is_search_input_present(self) -> bool:
        return self.is_visible(self.SEARCH_INPUT)
