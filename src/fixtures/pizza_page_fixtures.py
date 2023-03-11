from random import choice

import allure
import pytest

from src.data.site_links import MAIN_PAGE_URL
from src.data.test_data import ALL_PIZZA_LINKS
from src.models.main_page.slider import PizzaSlider


@pytest.fixture(scope="function")
def pizza_page(get_driver):
    with allure.step("Открытие страницы пиццы"):
        url = choice(ALL_PIZZA_LINKS)
        driver = get_driver
        driver.get(url)
    yield driver


@pytest.fixture(scope="function")
def slider(get_driver):
    with allure.step("Получение слайдера с пиццами"):
        driver = get_driver
        driver.get(MAIN_PAGE_URL)

        slider = PizzaSlider(driver)
    yield slider
