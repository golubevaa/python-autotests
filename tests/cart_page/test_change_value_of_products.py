from random import choice
from flaky import flaky
import allure
import pytest

from src.data.test_data import ADD_BORTS


@allure.feature("Корзина")
@allure.story("Изменение кол-ва товаров в корзине")
class TestChangeNumberOfPizzaAtCart:
    @allure.title("Уменьшение кол-ва пицц - несколько пицц одного вида в строке")
    @pytest.mark.sanity
    @flaky(max_runs=3)
    def test_change_non_single_pizza(self, prepared_cart_with_pizza):
        cart_page = prepared_cart_with_pizza
        row = cart_page.cart.get_first_row_by_row_amount_greater_then(1)
        name = row.name
        pizza_element = row.web_element
        target = row.amount - 1

        cart_page.send_keys_to_pizza_form(element=pizza_element, key=target)
        cart_page.click_to_update_cart_button()

        assert name in cart_page.cart.get_names_by_amount(target)

    @allure.title("Уменьшение кол-ва пицц - одна пицца одного вида в строке")
    @flaky(max_runs=3)
    def test_decrement_single_pizza(self, prepared_cart_with_pizza):
        cart_page = prepared_cart_with_pizza
        row = cart_page.cart.get_first_by_amount(1)
        pizza_element = row.web_element
        target = row.amount - 1

        cart_page.send_keys_to_pizza_form(element=pizza_element, key=target)
        cart_page.click_to_update_cart_button()

        assert cart_page.cart.get_names_by_amount(target) == []

    @pytest.mark.high_priority
    @allure.title("Уменьшение кол-ва пицц - одна пицца в корзине")
    def test_decrement_single_pizza_at_cart(self, prepared_cart_with_single_pizza):
        cart_page = prepared_cart_with_single_pizza
        row = cart_page.cart.get_first_by_amount(1).web_element
        target = 0

        cart_page.send_keys_to_pizza_form(element=row, key=target)
        cart_page.click_to_update_cart_button()

        assert cart_page.cart_is_empty()

    @allure.title("Изменение кол-ва пицц - пицца с доп. опциями")
    @pytest.mark.parametrize("add_option", ADD_BORTS)
    def test_change_pizza_value_with_add_option(self, prepared_cart_with_pizza, add_option):
        cart_page = prepared_cart_with_pizza
        row = cart_page.cart.get_first_by_add_option(add_option)
        pizza_element = row.web_element
        target = choice([i for i in range(1, 30) if i != row.amount])

        cart_page.send_keys_to_pizza_form(element=pizza_element, key=target)
        cart_page.click_to_update_cart_button()

        assert cart_page.cart.get_first_by_add_option(add_option).amount == target
