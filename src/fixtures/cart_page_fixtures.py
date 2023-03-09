import os

import pytest

from src.helpers.add_to_cart_at_product_page import go_to_pizza_page_and_add_to_cart
from src.models.cart_page.cart import CartTable

from src.utils.shiffle_properties import shuffle_pizza_props


@pytest.fixture(scope="function")
def prepared_cart_with_pizza(environment, get_driver):
    cart_page_url = os.getenv("cart_page_url")
    driver = get_driver
    params = shuffle_pizza_props()

    for param in params:
        go_to_pizza_page_and_add_to_cart(driver, param)

    driver.get(cart_page_url)
    cart = CartTable(driver)

    yield cart, driver


@pytest.fixture(scope="function")
def prepared_cart_with_single_pizza(environment, get_driver):
    cart_page_url = os.getenv("cart_page_url")
    driver = get_driver
    params = [element for element in shuffle_pizza_props() if element.options.value == 1][0]
    go_to_pizza_page_and_add_to_cart(driver, params)

    driver.get(cart_page_url)
    cart = CartTable(driver)

    yield cart, driver
