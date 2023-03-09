from random import choice

import pytest
import os

from src.models.main_page.slider import PizzaSlider
from src.utils.get_pizza_slider_info import get_all_possible_links


@pytest.fixture(scope="function")
def pizza_page(get_driver, environment):
    url = choice(get_all_possible_links())
    driver = get_driver
    driver.get(url)
    yield driver


@pytest.fixture(scope="function")
def slider(get_driver, environment):
    main_page_url = os.getenv("main_page_url")
    driver = get_driver
    driver.get(main_page_url)

    slider = PizzaSlider(driver)
    yield slider
