from random import choice

import allure
import pytest

from src.data.test_data import ALL_PIZZA_LINKS
from src.pages.main_page import MainPage
from src.pages.pizza_page import PizzaPage


@pytest.fixture(scope="function")
def pizza_page(get_driver):
    with allure.step("Открытие страницы пиццы"):
        url = choice(ALL_PIZZA_LINKS)
    yield PizzaPage(get_driver, url)


@pytest.fixture(scope="function")
def slider(get_driver):
    with allure.step("Получение слайдера с пиццами"):
        main_page = MainPage(get_driver)

        slider = main_page.slider
    yield slider


@pytest.fixture(scope="function")
def main_page(get_driver):
    yield MainPage(get_driver)
