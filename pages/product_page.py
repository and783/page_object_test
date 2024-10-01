from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def should_be_basket(self):
        self.click_add_to_basket()
        self.get_number()
        self.check_book()
        self.check_price()
    
    def click_add_to_basket(self):
        click_basket = self.browser.find_element(*ProductPageLocators.BASKET)
        click_basket.click()
        
    def get_number(self):
        time.sleep(2)
        self.solve_quiz_and_get_code()
        time.sleep(2)
        
    def check_book(self):
        book_name = self.browser.find_element(By.CSS_SELECTOR, ".col-sm-6.product_main h1").text
        add_book_name = self.browser.find_element(By.CSS_SELECTOR, ".alertinner strong").text
        assert book_name == add_book_name, " Ошибка, книги не совпадают"

    def check_price(self):
        price = self.browser.find_element(By.CSS_SELECTOR, ".product_main p.price_color").text
        price_in_basket = self.browser.find_element(By.CSS_SELECTOR, ".alertinner p strong").text
        assert price == price_in_basket, " Ошибка, цены не совпадают"
        time.sleep(3)
        
        
        
        
        
        
    
    

        
        
