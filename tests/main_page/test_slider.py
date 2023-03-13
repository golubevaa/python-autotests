import allure
import pytest

from src.data.test_data import ALL_PIZZA_NAMES, SLIDER_BUTTONS


@allure.feature("Главная страница")
@allure.story("Слайдер")
class TestMainPageSlider:

    @allure.title("Прокрутка слайдера на главной странице вправо/влево")
    @pytest.mark.sanity
    @pytest.mark.parametrize("slick_destination", SLIDER_BUTTONS,
                             ids=["slick to previous", "slick to next"])
    def test_slick_pizza_slider(self, slick_destination, slider):
        visible_pizzas = slider.get_names()

        getattr(slider, slick_destination)()
        new_visible_pizzas = slider.get_names()

        with allure.step("Сравнение списка видимых пицц до прокрутки и после"):
            assert visible_pizzas != new_visible_pizzas

    @allure.title("Появление кнопки 'В корзину' при наведении на пиццу")
    @pytest.mark.parametrize("current", ALL_PIZZA_NAMES)
    def test_add_to_cart_button_appearance(self, current, main_page):
        main_page.slick_slider_until_pizza_will_be_displayed(pizza_name=current)
        slider = main_page.slider

        add_to_cart_button = slider.get_add_to_cart_button(product=current)
        main_page.move_to_button(add_to_cart_button)

        with allure.step("Проверка что кнопка 'В корзину' видима"):
            assert add_to_cart_button.is_displayed()

    @allure.title("Появление кнопки 'В корзину' после добавления пиццы в корзину")
    @pytest.mark.skip(reason="known issue")
    @pytest.mark.parametrize("current", ALL_PIZZA_NAMES)
    def test_add_to_cart_button_appearance_when_add_to_cart(self, current, main_page):
        main_page.slick_slider_until_pizza_will_be_displayed(pizza_name=current)
        slider = main_page.slider

        main_page.add_to_cart(product=current)
        add_to_cart_button = slider.get_add_to_cart_button(product=current)

        with allure.step("Проверка что кнопка 'В корзину' видима"):
            assert add_to_cart_button.is_displayed()
