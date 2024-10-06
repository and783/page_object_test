import time
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        
    def should_be_login_url(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert "login" in self.browser.current_url, "Url is not correct"
        
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "QQ123!@#)*"
        add_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        add_email.send_keys(email)
        add_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        add_password.send_keys(password)
        add_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        add_password_confirm.send_keys(password)
        click_ragistration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        click_ragistration_button.click()
        
