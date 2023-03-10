from random import randint

import allure
import pytest
from selenium.common import TimeoutException

from src.data.test_data import ADD_BORTS, ALL_BORTS, SWITCH_OPTION


@allure.feature("Страницы пицц")
@allure.story("Дополнительные опции")
@pytest.mark.high_priority
class TestPizzaAddOptions:

    @allure.title("Проверка наличия дополнительных опций")
    def test_observe_doping(self, pizza_page):

        options = pizza_page.get_options_text()

        with allure.step("Проверка наличия всех доп. опций"):
            assert options == ALL_BORTS

    @allure.title("Проверка возможности выбора дополнительной опции")
    @pytest.mark.parametrize("doping_name", ALL_BORTS)
    def test_select_doping(self, pizza_page, doping_name):

        pizza_page.select_doping_by_name(doping_name)

        with allure.step("Выбрана верная дополнительная опция"):
            assert doping_name in pizza_page.doping_menu.first_selected_option.text

    @allure.title("Проверка изменения цены пиццы при выборе дополнительной опции")
    @pytest.mark.parametrize("doping_name", ADD_BORTS)
    def test_select_doping_and_change_price(self, pizza_page, doping_name):
        price_before_doping = pizza_page.get_price()
        doping_price = pizza_page.get_doping_price(doping_name)

        pizza_page.select_doping_by_name(doping_name)

        with allure.step("При выборе допинга цена пиццы изменилась на стоимость допинга"):
            assert pizza_page.get_price() == price_before_doping + doping_price

    @allure.title("Проверка возможности повторного переключения между опциями")
    @pytest.mark.parametrize("doping_name", ADD_BORTS)
    def test_select_doping_switch_between_options(self, pizza_page, doping_name):

        pizza_page.select_doping_by_name(name=doping_name)
        pizza_page.select_doping_by_name(name=SWITCH_OPTION)

        with allure.step("Дополнительная опция переключилась повторно"):
            assert pizza_page.doping_menu.first_selected_option.text == SWITCH_OPTION

    @allure.title("Количество пицц - увеличение значения инпут формы")
    def test_increase_pizza_counter(self, pizza_page):
        increase_value = str(randint(2, 30))

        new_value = pizza_page.send_keys_to_input_form(key=increase_value)

        with allure.step("Количество пицц можно увеличить с помощью инпут формы"):
            assert new_value == increase_value

    @allure.title("Попытка добавить 0 пицц в корзину")
    def test_add_zero_pizza_to_cart(self, pizza_page):
        prev_cart_sum = pizza_page.cart_text

        pizza_page.send_keys_to_input_form(key=0)

        with pytest.raises(TimeoutException):
            pizza_page.add_to_cart()

        with allure.step("Цена продуктов в корзине не изменилась"):
            assert prev_cart_sum == pizza_page.cart_text
