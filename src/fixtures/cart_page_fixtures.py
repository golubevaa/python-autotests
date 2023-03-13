import allure
import pytest

from src.helpers.add_to_cart_at_product_page import go_to_pizza_page_and_add_to_cart
from src.pages.cart_page import CartPage

from src.utils.shiffle_properties import shuffle_pizza_props


@pytest.fixture(scope="function")
def prepared_cart_with_pizza(get_driver):
    with allure.step("Получение корзины с пиццами со всеми вариациями допов"):
        driver = get_driver
        params = shuffle_pizza_props()
        for param in params:
            go_to_pizza_page_and_add_to_cart(driver, param)

        cart_page = CartPage(driver)
    yield cart_page


@pytest.fixture(scope="function")
def prepared_cart_with_single_pizza(get_driver):
    with allure.step("Получение корзины с одной пиццей со случайным допом внутри"):
        driver = get_driver
        params = [element for element in shuffle_pizza_props() if element.options.value == 1][0]
        go_to_pizza_page_and_add_to_cart(driver, params)

        cart_page = CartPage(driver)
    yield cart_page
