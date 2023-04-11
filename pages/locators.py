from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    ITEM_NAME_TEXT = (By.CSS_SELECTOR, '.product_main > h1')
    ITEM_PRICE_TEXT = (By.CSS_SELECTOR, '.product_main > .price_color')

    # [Товар] был добавлен в вашу корзину
    SUCCESS_ADD_TO_BASKET_ITEM_TEXT = (By.CSS_SELECTOR, '#messages > .alert-success > .alertinner')

    # Стоимость корзины теперь составляет [Общая стоимость]
    SUCCESS_NOW_BASKET_PRICE_TEXT = (By.CSS_SELECTOR, '#messages > .alert-info > .alertinner > p')
