from random import randint

import allure
import pytest

from src.actions.common_actions import get_cart_text
from src.actions.pizza_page_actions.pizza_page_actions import (
    get_doping_options_text, select_doping_by_name, find_doping_menu, get_pizza_price, get_doping_price,
    send_keys_to_input_form, click_to_add_to_cart
)
from src.data.test_data import ADD_BORTS, ALL_BORTS


@allure.feature("Страницы пицц")
@allure.story("Дополнительные опции")
@pytest.mark.high_priority
class TestPizzaAddOptions:

    @allure.title("Проверка наличия дополнительных опций")
    def test_observe_doping(self, pizza_page):
        driver = pizza_page

        options = get_doping_options_text(driver,
                                          without_cost=True)
        assert options == ALL_BORTS

    @allure.title("Проверка возможности выбора дополнительной опции")
    @pytest.mark.parametrize("doping_name", ALL_BORTS)
    def test_select_doping(self, pizza_page, doping_name):
        driver = pizza_page
        menu = find_doping_menu(driver)

        select_doping_by_name(menu=menu,
                              name=doping_name)

        assert doping_name in menu.first_selected_option.text

    @allure.title("Проверка изменения цены пиццы при выборе дополнительной опции")
    @pytest.mark.parametrize("doping_name", ADD_BORTS)
    def test_select_doping_and_change_price(self, pizza_page, doping_name):
        driver = pizza_page
        price_before_doping = get_pizza_price(driver)
        menu = find_doping_menu(driver)
        doping_price = get_doping_price(menu=menu,
                                        name=doping_name)

        select_doping_by_name(menu=menu,
                              name=doping_name)

        assert get_pizza_price(driver) == price_before_doping + doping_price

    @allure.title("Проверка возможности повторного переключения между опциями")
    @pytest.mark.parametrize("doping_name", ADD_BORTS)
    def test_select_doping_switch_between_options(self, pizza_page, doping_name):
        driver = pizza_page
        switch_option = "Обычный"
        menu = find_doping_menu(driver)

        select_doping_by_name(menu=menu,
                              name=doping_name)
        select_doping_by_name(menu=menu,
                              name=switch_option)

        assert menu.first_selected_option.text == switch_option

    @allure.title("Количество пицц - увеличение значения инпут формы")
    def test_increase_pizza_counter(self, pizza_page):
        driver = pizza_page
        increase_value = str(randint(2, 30))

        new_input_form = send_keys_to_input_form(driver=driver,
                                                 key=increase_value)

        assert new_input_form.get_attribute('value') == increase_value

    @allure.title("Попытка добавить 0 пицц в корзину")
    def test_add_zero_pizza_to_cart(self, pizza_page):
        driver = pizza_page
        increase_value = "0"
        prev_cart_sum = get_cart_text(driver)

        send_keys_to_input_form(driver=driver,
                                key=increase_value)
        click_to_add_to_cart(driver)

        assert prev_cart_sum == get_cart_text(driver)
