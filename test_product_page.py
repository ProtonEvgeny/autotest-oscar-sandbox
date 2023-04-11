from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('num_promo', [str(i) for i in range(0, 10)])
def test_guest_can_add_product_to_basket(browser, num_promo):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num_promo}'
    page = ProductPage(browser, link)
    page.open()
    page.item_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_in_basket()
    page.should_be_basket_price()
