from random import choice
import allure
import pytest
from src.pages.cart_page import CartPage


@allure.feature("Главная страница")
@allure.story("Добавление товаров в корзину")
class TestMainPageAddToCart:

    @allure.title("Отображение цены продукта в корзине при его добавлении")
    @pytest.mark.sanity
    def test_cart_content(self, main_page):
        slider = main_page.slider
        pizza_to_test = choice(slider.visible_pizzas).name

        pizza_in_cart, total_cost = main_page.add_pizza_from_slider_to_cart(pizza=pizza_to_test,
                                                                            pizza_in_cart=[])

        with allure.step("Проверка что цена продуктов в корзине изменилась"):
            assert total_cost == main_page.get_cart_text()

    @allure.title("Проверка добавления пиццы в корзину - переход с помощью значка корзины")
    @pytest.mark.high_priority
    def test_go_to_cart_using_cart_label(self, main_page):
        slider = main_page.slider
        pizza_to_test = choice(slider.visible_pizzas).name

        pizza_in_cart, total_cost = main_page.add_pizza_from_slider_to_cart(pizza=pizza_to_test,
                                                                            pizza_in_cart=[])

        main_page.go_to_cart_using_cart_contents()
        cart_page = CartPage(main_page.driver)

        with allure.step("Проверка что в корзине 1 продукт"):
            assert cart_page.cart.count_products() == 1
        with allure.step("Проверка что добавлена верная пицца"):
            assert cart_page.cart.get_by_index(0).name.lower() == pizza_in_cart[0]

    @allure.title("Проверка добавления пиццы в корзину - переход с помощью общего меню")
    def test_go_to_cart_using_head_button(self, main_page):
        slider = main_page.slider
        pizza_to_test = choice(slider.visible_pizzas).name

        pizza_in_cart, total_cost = main_page.add_pizza_from_slider_to_cart(pizza=pizza_to_test,
                                                                            pizza_in_cart=[])

        main_page.go_to_cart_via_menu()
        cart_page = CartPage(main_page.driver)

        with allure.step("Проверка что в корзине 1 продукт"):
            assert cart_page.cart.count_products() == 1
        with allure.step("Проверка что добавлена верная пицца"):
            assert cart_page.cart.get_by_index(0).name.lower() == pizza_in_cart[0]
