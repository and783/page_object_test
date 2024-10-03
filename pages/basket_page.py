import time
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By



class BasketPage(BasePage):
    def basket_is_clear(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_CLEAR_BASKET), "Books added in basket"
       
    def check_clear_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.CLEAR_BASKET), "Books added in basket"
    

    
