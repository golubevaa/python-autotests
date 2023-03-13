import allure
import pytest

from src.data.test_data import ALL_PIZZA_NAMES
from src.locators.main_page_locators import MainPageLocators as Locators


@allure.feature("Главная страница")
@allure.story("Слайдер")
class TestMainPageSlider:

    @allure.title("Прокрутка слайдера на главной странице вправо/влево")
    @pytest.mark.sanity
    @pytest.mark.parametrize("slick_destination", [Locators.slider_slick_prev, Locators.slider_slick_next],
                             ids=["slick to previous", "slick to next"])
    def test_slick_pizza_slider(self, slick_destination, slider):
        visible_pizzas = slider.get_names()

        getattr(slider, slick_destination.replace("-", "_"))()
        new_visible_pizzas = slider.get_names()

        assert visible_pizzas != new_visible_pizzas

    @allure.title("Появление кнопки 'В корзину' при наведении на пиццу")
    @pytest.mark.parametrize("current", ALL_PIZZA_NAMES)
    def test_add_to_cart_button_appearance(self, current, main_page):
        main_page.slick_slider_until_pizza_will_be_displayed(pizza_name=current)
        slider = main_page.slider

        add_to_cart_button = slider.get_add_to_cart_button(product=current)
        main_page.move_to_button(add_to_cart_button)

        assert add_to_cart_button.is_displayed()

    @allure.title("Появление кнопки 'В корзину' после добавления пиццы в корзину")
    @pytest.mark.skip(reason="known issue")
    @pytest.mark.parametrize("current", ALL_PIZZA_NAMES)
    def test_add_to_cart_button_appearance_when_add_to_cart(self, current, main_page):
        main_page.slick_slider_until_pizza_will_be_displayed(pizza_name=current)
        slider = main_page.slider

        main_page.add_to_cart(product=current)
        add_to_cart_button = slider.get_add_to_cart_button(product=current)

        assert add_to_cart_button.is_displayed()
