import allure
import pytest
from random import randint

from src.actions.pizza_page_actions.pizza_page_actions import (
    send_keys_to_input_form, get_pizza_title, find_doping_menu, select_doping_by_name
)
from src.helpers.get_cart_content_after_adding_pizza import add_to_cart_and_get_content


class TestAddPizzaToCartFromPage:

    @allure.title("Проверка добавления верной пиццы в корзину")
    @pytest.mark.parametrize("execution_number", range(3))
    def test_names_of_pizza_in_cart(self, pizza_page, execution_number):
        driver = pizza_page
        title = get_pizza_title(driver)

        cart = add_to_cart_and_get_content(driver)

        assert cart.get_name_by_index(0).lower() == title

    @allure.title("Проверка добавления верного количества пицц в корзину")
    @pytest.mark.parametrize('pizza_to_add', [str(randint(1, 30)) for _ in range(3)])
    def test_add_several_pizza_to_cart(self, pizza_page, pizza_to_add):
        driver = pizza_page

        send_keys_to_input_form(driver=driver,
                                key=pizza_to_add)
        cart = add_to_cart_and_get_content(driver)

        assert cart.count_products() == int(pizza_to_add)

    @allure.title("Добавление пиццы с дополнительной опцией в корзину")
    @pytest.mark.parametrize("add_option", ["Сырный", "Колбасный"])
    def test_add_pizza_with_add_option(self, pizza_page, add_option):
        driver = pizza_page

        menu = find_doping_menu(driver)
        select_doping_by_name(menu=menu,
                              name=add_option)
        cart = add_to_cart_and_get_content(driver)

        assert add_option in cart.cart_rows[0].additional_option
