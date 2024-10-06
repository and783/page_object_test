import time
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_basket(self):
        self.click_add_to_basket()
        
    def click_add_to_basket(self):
        click_basket = self.browser.find_element(*ProductPageLocators.BASKET)
        click_basket.click()
        
    def get_number(self):
        time.sleep(2)
        self.solve_quiz_and_get_code()
        time.sleep(3)
        
    def check_book(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        add_book_name = self.browser.find_element(*ProductPageLocators.ADD_BOOK_NAME).text
        assert book_name == add_book_name, "Error, books not match"

    def check_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert price == price_in_basket, "Error, books not match"
        time.sleep(2)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        
        
        
        
        
        
    
    

        
        
