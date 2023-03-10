import allure
import pytest

from random import choice, sample

from src.actions.common_actions import get_cart_text, go_to_cart_via_menu, go_to_cart_using_cart_contents
from src.actions.main_page_actions.main_page_actions import add_pizza_from_slider_to_cart
from src.models.cart_page.cart import CartTable
from src.waits.common_waits import wait_for_cart_info_changes


class TestMainPageAddToCart:

    @allure.title("Отображение цены продукта в корзине при его добавлении")
    @pytest.mark.parametrize("pizza_to_add", [1, 2])
    def test_cart_content(self, slider, pizza_to_add):
        driver = slider.driver
        pizza_to_test = sample(slider.visible_pizzas, k=pizza_to_add)
        empty_cart_info = get_cart_text(driver)

        pizza_in_cart, total_cost = add_pizza_from_slider_to_cart(pizza_list=pizza_to_test,
                                                                  pizza_in_cart=[])
        wait_for_cart_info_changes(driver=driver,
                                   prev_cart_info=empty_cart_info)

        assert total_cost == get_cart_text(driver)

    @allure.title("Проверка добавления пиццы в корзину - переход с помощью значка корзины")
    def test_go_to_cart_using_cart_label(self, slider):
        driver = slider.driver
        pizza_in_cart, total_cost = add_pizza_from_slider_to_cart(pizza_list=[choice(slider.visible_pizzas)],
                                                                  pizza_in_cart=[])

        go_to_cart_using_cart_contents(driver)
        cart = CartTable(driver)

        assert cart.count_products() == 1
        assert cart.get_by_index(0).name == pizza_in_cart[0].lower()

    @allure.title("Проверка добавления пиццы в корзину - переход с помощью общего меню")
    def test_go_to_cart_using_head_button(self, slider):
        driver = slider.driver
        pizza_in_cart, total_cost = add_pizza_from_slider_to_cart(pizza_list=[choice(slider.visible_pizzas)],
                                                                  pizza_in_cart=[])
        go_to_cart_via_menu(driver)
        cart = CartTable(driver)

        assert cart.count_products() == 1
        assert cart.get_by_index(0).name == pizza_in_cart[0].lower()
