from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, f'URL is not correct. Should be login URL.'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), f'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), f'Registration form is not presented'

    def register_new_user(self, email: str, password: str):
        self.should_be_login_page()
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)
        pass1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS1)
        pass1_field.send_keys(password)
        pass2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS2)
        pass2_field.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        reg_button.click()
