from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    def open(self, url: str):
        self.driver.get(url)

    def find(self, locator: tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator: tuple):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator: tuple, text: str):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        return self.find_visible(locator).text

    def is_visible(self, locator: tuple) -> bool:
        try:
            return self.find_visible(locator).is_displayed()
        except Exception:
            return False

    def get_title(self) -> str:
        return self.driver.title

    def get_url(self) -> str:
        return self.driver.current_url
