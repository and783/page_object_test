from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_is_clear(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_CLEAR_BASKET), "Books added in basket"
       
    def check_clear_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.CLEAR_BASKET), "Books added in basket"

    def open_basket_page(self):
        open_basket = self.browser.find_element(*BasketPageLocators.OPEN_BASKET)
        open_basket.click()
    

    
