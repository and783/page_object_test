import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
import time


@pytest.mark.parametrize('link', ["offer0", "offer1", "offer2", "offer3","offer4", "offer5",
                                  "offer6", pytest.param("offer7", marks=pytest.mark.xfail),
                                  "offer8", "offer9"])

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link): 
    browser.delete_all_cookies()
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={link}" 
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.get_number()
    page.check_book()
    page.check_price()

@pytest.mark.skip #xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.should_not_be_success_message()
    
@pytest.mark.skip #delete after test
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip #xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.should_be_disappeared()
    
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page_login = LoginPage(browser, link)
    page_login.should_be_login_form()
    page_login.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page_go_basket = BasePage(browser, link)
    page_go_basket.open_basket_page()
    page.basket_is_clear()
    page.check_clear_basket()
    
    



    
