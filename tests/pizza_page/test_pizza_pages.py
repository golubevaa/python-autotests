import allure
import pytest


from src.data.test_data import ALL_PIZZA_NAMES
from src.pages.pizza_page import PizzaPage


@allure.feature("Страницы пицц")
@allure.story("Переход на страницу пиццы с главной страницы сайта")
class TestGoToPizzaPage:

    @allure.title("Переход на страницу пиццы с помощью слайдера")
    @pytest.mark.parametrize('pizza', ALL_PIZZA_NAMES)
    def test_go_to_current_pizza_page(self, pizza, main_page):
        main_page.slick_slider_until_pizza_will_be_displayed(pizza_name=pizza)
        driver = main_page.driver

        url = main_page.open_pizza_page(pizza)
        pizza_page = PizzaPage(driver, url)

        assert pizza_page.product_title == pizza
