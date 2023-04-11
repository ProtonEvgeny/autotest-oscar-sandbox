from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_item_name(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME_TEXT), f'Item name is not presented'

    def should_be_success_add_to_basket_item(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_ITEM_TEXT), \
            f'Success add to basket message is not presented'

    def should_be_item_price(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE_TEXT), f'Item price is not presented'

    def should_be_success_now_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_NOW_BASKET_PRICE_TEXT), \
            f'Success now basket price message is not presented'

    def item_add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_in_basket(self):
        self.should_be_item_name()
        self.should_be_success_add_to_basket_item()

        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME_TEXT).text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_ITEM_TEXT).text
        basket_item_true = item_name in success_message

        assert basket_item_true, f'Expected: "{item_name} [success message in chosen language]"\n' \
                                 f'Actual: "{success_message}"'

    def should_be_basket_price(self):
        self.should_be_item_price()
        self.should_be_success_now_basket_price()

        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_TEXT).text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_NOW_BASKET_PRICE_TEXT).text
        basket_price_true = item_price in success_message

        assert basket_price_true, f'Expected: "[success message in chosen language] {item_price}"\n' \
                                  f'Actual: "{success_message}"'
