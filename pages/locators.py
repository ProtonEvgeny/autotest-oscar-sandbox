from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini > .btn-group > a')
    BASKET_LINK_INVALID = (By.CSS_SELECTOR, '.basket-mini_inc > .btn-group > a')


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    ITEM_NAME_TEXT = (By.CSS_SELECTOR, '.product_main > h1')
    ITEM_PRICE_TEXT = (By.CSS_SELECTOR, '.product_main > .price_color')

    # [Товар] был добавлен в вашу корзину
    SUCCESS_ADD_TO_BASKET_ITEM_TEXT = (By.CSS_SELECTOR, '#messages > .alert-success > .alertinner > strong')

    # Стоимость корзины теперь составляет [Общая стоимость]
    SUCCESS_NOW_BASKET_PRICE_TEXT = (By.CSS_SELECTOR, '#messages > .alert-info > .alertinner > p > strong')


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, '#basket_formset')
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
