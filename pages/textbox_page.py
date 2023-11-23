from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TextBoxLocators:
    LOCATOR_FULL_NAME = (By.TAG_NAME, "input")
    LOCATOR_FULL_EMAIL = (By.ID, "userEmail")
    LOCATOR_FILL_ADDRESS = (By.XPATH, "//*[@id='currentAddress']")
    LOCATOR_FILL_PERMANENT_ADDRESS = (By.XPATH, "//*[@id='permanentAddress']")
    LOCATOR_SUBMIT = (By.ID, "submit")
    LOCATOR_CHECK = (By.XPATH, "//*[@id='name']")

    LOCATOR_CREATED_NAME = (By.CSS_SELECTOR, "#output #userName")
    LOCATOR_CREATED_EMAIL = (By.CSS_SELECTOR, "#output #userEmail")
    LOCATOR_CREATED_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    LOCATOR_CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress")


class TextBox(BasePage):

    # Full Name
    def fill_username(self, username):
        fill_username = self.find_element(TextBoxLocators.LOCATOR_FULL_NAME)
        fill_username.send_keys(username)

    # Email
    def fill_email(self, email):
        fill_email = self.find_element(TextBoxLocators.LOCATOR_FULL_EMAIL)
        fill_email.send_keys(email)

    # Current Address
    def fill_address(self, address):
        fill_address = self.find_element(TextBoxLocators.LOCATOR_FILL_ADDRESS)
        fill_address.send_keys(address)

    # Permanent Address
    def fill_permanent_address(self, permanent_address):
        fill_permanent_address = self.find_element(TextBoxLocators.LOCATOR_FILL_PERMANENT_ADDRESS)
        fill_permanent_address.send_keys(permanent_address)

    def submit(self):
        self.find_element(TextBoxLocators.LOCATOR_SUBMIT).click()

    # def check(self):
    #     username = self.(TextBoxLocators.LOCATOR_CREATED_NAME)
    #     email = self.find_element(TextBoxLocators.LOCATOR_CREATED_EMAIL)
    #     address = self.find_element(TextBoxLocators.LOCATOR_CREATED_ADDRESS)
    #     permanent_address = self.find_element(TextBoxLocators.LOCATOR_CREATED_PERMANENT_ADDRESS)
    #
