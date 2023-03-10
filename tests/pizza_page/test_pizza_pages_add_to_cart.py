import allure
import pytest

from src.data.test_data import ADD_BORTS, INT_SAMPLE
from src.pages.cart_page import CartPage


@allure.feature("Страницы пицц")
@allure.story("Добавление в корзину")
class TestAddPizzaToCartFromPage:

    @allure.title("Проверка добавления верной пиццы в корзину")
    def test_names_of_pizza_in_cart(self, pizza_page):
        pizza_title = pizza_page.cart_format_product_title
        driver = pizza_page.driver

        pizza_page.add_to_cart()
        pizza_page.go_to_cart_using_cart_contents()
        cart = CartPage(driver).cart

        with allure.step("В корзину добавлена верная пицца"):
            assert cart.get_by_index(0).name == pizza_title

    @allure.title("Проверка добавления верного количества пицц в корзину")
    @pytest.mark.parametrize('pizza_to_add', INT_SAMPLE)
    def test_add_several_pizza_to_cart(self, pizza_page, pizza_to_add):
        pizza_page.send_keys_to_input_form(key=pizza_to_add)
        driver = pizza_page.driver

        pizza_page.add_to_cart()
        pizza_page.go_to_cart_using_cart_contents()
        cart = CartPage(driver).cart

        with allure.step("В корзину добавлено верное кол-во пицц"):
            assert cart.count_products() == pizza_to_add

    @allure.title("Добавление пиццы с дополнительной опцией в корзину")
    @pytest.mark.parametrize("add_option", ADD_BORTS)
    def test_add_pizza_with_add_option(self, pizza_page, add_option):
        pizza_page.select_doping_by_name(name=add_option)
        driver = pizza_page.driver

        pizza_page.add_to_cart()
        pizza_page.go_to_cart_via_menu()
        cart = CartPage(driver).cart

        with allure.step("В корзину добавлена пицца с верной доп. опцией"):
            assert add_option in cart.cart_rows[0].additional_option
