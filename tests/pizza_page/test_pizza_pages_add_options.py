from random import randint

import allure
import pytest
from src.data.test_data import ADD_BORTS, ALL_BORTS


@allure.feature("Страницы пицц")
@allure.story("Дополнительные опции")
@pytest.mark.high_priority
class TestPizzaAddOptions:

    @allure.title("Проверка наличия дополнительных опций")
    def test_observe_doping(self, pizza_page):

        options = pizza_page.get_options_text()

        assert options == ALL_BORTS

    @allure.title("Проверка возможности выбора дополнительной опции")
    @pytest.mark.parametrize("doping_name", ALL_BORTS)
    def test_select_doping(self, pizza_page, doping_name):

        pizza_page.select_doping_by_name(doping_name)

        assert doping_name in pizza_page.doping_menu.first_selected_option.text

    @allure.title("Проверка изменения цены пиццы при выборе дополнительной опции")
    @pytest.mark.parametrize("doping_name", ADD_BORTS)
    def test_select_doping_and_change_price(self, pizza_page, doping_name):
        price_before_doping = pizza_page.get_price()
        doping_price = pizza_page.get_doping_price(doping_name)

        pizza_page.select_doping_by_name(doping_name)

        assert pizza_page.get_price() == price_before_doping + doping_price

    @allure.title("Проверка возможности повторного переключения между опциями")
    @pytest.mark.parametrize("doping_name", ADD_BORTS)
    def test_select_doping_switch_between_options(self, pizza_page, doping_name):
        switch_option = "Обычный"

        pizza_page.select_doping_by_name(name=doping_name)
        pizza_page.select_doping_by_name(name=switch_option)

        assert pizza_page.doping_menu.first_selected_option.text == switch_option

    @allure.title("Количество пицц - увеличение значения инпут формы")
    def test_increase_pizza_counter(self, pizza_page):
        increase_value = str(randint(2, 30))

        new_value = pizza_page.send_keys_to_input_form(key=increase_value)

        assert new_value == increase_value

    @allure.title("Попытка добавить 0 пицц в корзину")
    def test_add_zero_pizza_to_cart(self, pizza_page):
        increase_value = "0"
        prev_cart_sum = pizza_page.get_cart_text()

        pizza_page.send_keys_to_input_form(key=increase_value)
        pizza_page.add_to_cart()

        assert prev_cart_sum == pizza_page.get_cart_text()
