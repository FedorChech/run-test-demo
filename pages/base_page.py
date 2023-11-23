from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demoqa.com/text-box"

    def find_element(self, locator, time: int = 2):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator, time: int = 10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def element_is_present(self, locator, time: int = 10):
        return WebDriverWait(self, driver, time).until(EC.presence_of_element_located(locator))

    def go_to_site(self):
        self.driver.get(self.base_url)
