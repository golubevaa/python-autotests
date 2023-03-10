from random import choice

import pytest

from src.data.test_data import MAIN_PAGE_URL
from src.models.main_page.slider import PizzaSlider
from src.utils.get_pizza_slider_info import get_all_possible_links


@pytest.fixture(scope="function")
def pizza_page(get_driver):
    url = choice(get_all_possible_links())
    driver = get_driver
    driver.get(url)
    yield driver


@pytest.fixture(scope="function")
def slider(get_driver):
    driver = get_driver
    driver.get(MAIN_PAGE_URL)

    slider = PizzaSlider(driver)
    yield slider
