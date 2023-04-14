from .pages.product_page import ProductPage
import pytest


@pytest.mark.skip(reason='not now')
@pytest.mark.parametrize('num_promo', ['0', '1', '2', '3', '4', '5', '6',
                                       pytest.param('7', marks=pytest.mark.xfail(reason='known trivial bug')),
                                       '8', '9'])
def test_guest_can_add_product_to_basket(browser, num_promo):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num_promo}'
    page = ProductPage(browser, link)
    page.open()
    page.item_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_in_basket()
    page.should_be_basket_price()


@pytest.mark.skip(reason='known bug')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.item_add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip(reason='known bug')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.item_add_to_basket()
    page.should_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
