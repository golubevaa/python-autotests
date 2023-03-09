import allure
import pytest

from src.actions.common_actions import get_cart_text
from src.actions.main_page_actions.main_page_actions import (
    get_add_to_cart_button, move_to_add_to_cart, add_product_to_cart, slick_slider_until_pizza_will_be_displayed
)
from src.utils.get_pizza_slider_info import get_all_possible_names
from src.waits.common_waits import wait_for_cart_info_changes


class TestMainPageSlider:

    @allure.title("Прокрутка слайдера на главной странице вправо/влево")
    @pytest.mark.parametrize("slick_destination", ["slick_next", "slick_prev"])
    def test_slick_pizza_slider(self, slick_destination, slider):
        visible_pizzas = slider.get_names()

        getattr(slider, slick_destination)()
        new_visible_pizzas = slider.get_names()

        assert visible_pizzas != new_visible_pizzas

    @pytest.mark.parametrize("current", get_all_possible_names())
    @allure.title("Появление кнопки 'В корзину' при наведении на пиццу")
    def test_add_to_cart_button_appearance(self, current, slider):
        slick_slider_until_pizza_will_be_displayed(slider=slider, pizza_name=current)

        pizza = slider.get_by_name(current).web_element
        add_to_cart_button = get_add_to_cart_button(pizza)
        move_to_add_to_cart(pizza)

        assert add_to_cart_button.is_displayed()

    @pytest.mark.skip(reason="known issue")
    @pytest.mark.parametrize("current", get_all_possible_names())
    @allure.title("Появление кнопки 'В корзину' после добавления пиццы в корзину")
    def test_add_to_cart_button_appearance_when_add_to_cart(self, current, slider):
        slick_slider_until_pizza_will_be_displayed(slider=slider, pizza_name=current)
        pizza = slider.get_by_name(current).web_element
        add_to_cart_button = get_add_to_cart_button(pizza)
        empty_cart_info = get_cart_text(slider.driver)

        add_product_to_cart(pizza)
        wait_for_cart_info_changes(driver=slider.driver,
                                   prev_cart_info=empty_cart_info)

        assert add_to_cart_button.is_displayed()
