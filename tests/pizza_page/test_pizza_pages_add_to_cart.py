import allure
import pytest

from src.actions.pizza_page_actions.pizza_page_actions import (
    send_keys_to_input_form, get_pizza_title, find_doping_menu, select_doping_by_name
)
from src.data.test_data import ADD_BORTS, INT_SAMPLE
from src.helpers.get_cart_content_after_adding_pizza import add_to_cart_and_get_content


@allure.feature("Страницы пицц")
@allure.story("Добавление в корзину")
class TestAddPizzaToCartFromPage:

    @allure.title("Проверка добавления верной пиццы в корзину")
    def test_names_of_pizza_in_cart(self, pizza_page):
        driver = pizza_page
        title = get_pizza_title(driver)

        cart = add_to_cart_and_get_content(driver)

        assert cart.get_by_index(0).name.lower() == title

    @allure.title("Проверка добавления верного количества пицц в корзину")
    @pytest.mark.parametrize('pizza_to_add', INT_SAMPLE)
    def test_add_several_pizza_to_cart(self, pizza_page, pizza_to_add):
        driver = pizza_page

        send_keys_to_input_form(driver=driver,
                                key=pizza_to_add)
        cart = add_to_cart_and_get_content(driver)

        assert cart.count_products() == pizza_to_add

    @allure.title("Добавление пиццы с дополнительной опцией в корзину")
    @pytest.mark.parametrize("add_option", ADD_BORTS)
    def test_add_pizza_with_add_option(self, pizza_page, add_option):
        driver = pizza_page

        menu = find_doping_menu(driver)
        select_doping_by_name(menu=menu,
                              name=add_option)
        cart = add_to_cart_and_get_content(driver)

        assert add_option in cart.cart_rows[0].additional_option
