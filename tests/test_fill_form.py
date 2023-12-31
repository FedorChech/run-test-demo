import pytest
import allure
from pages.textbox_page import TextBox
import time


@pytest.mark.positive
def test_fill_form_1(browser):
    main_page = TextBox(browser)
    main_page.go_to_site()
    main_page.fill_username("Fedor")
    main_page.fill_email("Fedor@gmail.com")
    main_page.fill_address("Novgorodskaya 20")
    main_page.fill_permanent_address("LKJDALKJSDLA")
    main_page.submit()
    time.sleep(5)


@pytest.mark.positive
def test_fill_form_2(browser):
    main_page = TextBox(browser)
    main_page.go_to_site()
    main_page.fill_username("Fedor")
    main_page.fill_email("Fedor@gmail.com")
    main_page.fill_address("Novgorodskaya 20")
    main_page.fill_permanent_address("LKJDALKJSDLA")
    main_page.submit()
    time.sleep(5)
