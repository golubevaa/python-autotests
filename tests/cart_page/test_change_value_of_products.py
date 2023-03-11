from random import choice

import allure
import pytest

from src.actions.cart_page_actions.cart_page_actions import (
    send_keys_to_number_of_pizza_form, click_to_update_cart_button, cart_is_empty
)
from src.data.test_data import ADD_BORTS


@allure.feature("Корзина")
@allure.story("Изменение кол-ва товаров в корзине")
class TestChangeNumberOfPizzaAtCart:
    @allure.title("Уменьшение кол-ва пицц - несколько пицц одного вида в строке")
    @pytest.mark.sanity
    def test_change_non_single_pizza(self, prepared_cart_with_pizza):
        cart, driver = prepared_cart_with_pizza
        row = cart.get_first_row_by_row_amount_greater_then(1)
        name = row.name
        target = str(row.amount - 1)

        send_keys_to_number_of_pizza_form(pizza_row=row.web_element, key=target)
        click_to_update_cart_button(driver)
        cart.update()

        assert name in cart.get_names_by_amount(int(target))

    @allure.title("Уменьшение кол-ва пицц - одна пицца одного вида в строке")
    def test_decrement_single_pizza(self, prepared_cart_with_pizza):
        cart, driver = prepared_cart_with_pizza
        row = cart.get_first_by_amount(1)
        target = str(row.amount - 1)

        send_keys_to_number_of_pizza_form(pizza_row=row.web_element, key=target)
        click_to_update_cart_button(driver)
        cart.update()

        assert cart.get_names_by_amount(int(target)) == []

    @pytest.mark.high_priority
    @allure.title("Уменьшение кол-ва пицц - одна пицца в корзине")
    def test_decrement_single_pizza_at_cart(self, prepared_cart_with_single_pizza):
        cart, driver = prepared_cart_with_single_pizza
        row = cart.get_first_by_amount(1)
        target = 0

        send_keys_to_number_of_pizza_form(pizza_row=row.web_element, key=target)
        click_to_update_cart_button(driver)

        assert cart_is_empty(driver)

    @allure.title("Изменение кол-ва пицц - пицца с доп. опциями")
    @pytest.mark.parametrize("add_option", ADD_BORTS)
    def test_change_pizza_value_with_add_option(self, prepared_cart_with_pizza, add_option):
        cart, driver = prepared_cart_with_pizza
        row = cart.get_first_by_add_option(add_option)
        target = choice([i for i in range(1, 30) if i != row.amount])

        send_keys_to_number_of_pizza_form(pizza_row=row.web_element, key=target)
        click_to_update_cart_button(driver)
        cart.update()

        assert cart.get_first_by_add_option(add_option).amount == target
