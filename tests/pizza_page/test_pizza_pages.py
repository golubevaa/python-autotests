import allure
import pytest


from src.actions.pizza_page_actions.pizza_page_actions import open_pizza_page, get_pizza_title
from src.actions.main_page_actions.main_page_actions import slick_slider_until_pizza_will_be_displayed
from src.data.test_data import ALL_PIZZA_NAMES
from src.waits.pizza_page_waits import wait_for_loading_pizza_page


@allure.feature("Страницы пицц")
@allure.story("Переход на страницу пиццы с главной страницы сайта")
class TestGoToPizzaPage:

    @allure.title("Переход на страницу пиццы с помощью слайдера")
    @pytest.mark.parametrize('pizza', ALL_PIZZA_NAMES)
    def test_go_to_current_pizza_page(self, pizza, slider):
        driver = slider.driver
        slick_slider_until_pizza_will_be_displayed(slider=slider,
                                                   pizza_name=pizza)

        open_pizza_page(pizza_element=slider.get_by_name(pizza).web_element)
        wait_for_loading_pizza_page(driver)

        assert get_pizza_title(driver, replace_quotes=False) == pizza.lower()
