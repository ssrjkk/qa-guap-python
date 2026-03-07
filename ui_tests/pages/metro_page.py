from selenium.webdriver.common.by import By
from .base_page import BasePage

class SpbMetroPage(BasePage):
    URL = "https://www.metro.spb.ru"

    HEADER = (By.TAG_NAME, "header")
    NAVIGATION = (By.CSS_SELECTOR, "nav, .nav-menu, .main-menu")
    MAP_LINK = (By.PARTIAL_LINK_TEXT, "схем")
    NEWS_SECTION = (By.CSS_SELECTOR, ".news, [class*='news'], [id*='news']")

    def open(self):
        super().open(self.URL)

    def is_page_loaded(self) -> bool:
        return self.is_visible(self.HEADER)

    def get_page_title(self) -> str:
        return self.get_title()

    def get_url(self) -> str:
        return self.driver.current_url
