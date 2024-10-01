import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage

@pytest.mark.parametrize('link', ["offer0", "offer1", "offer2", "offer3","offer4", "offer5",
                                  "offer6", pytest.param("offer7", marks=pytest.mark.xfail),
                                  "offer8", "offer9"])



def test_guest_can_add_product_to_basket(browser, link):
    browser.delete_all_cookies()
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={link}"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.get_number()
    page.check_book()
    page.check_price()
