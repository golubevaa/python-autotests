import allure
from random import choice, randint

from src.actions.pizza_page_actions.pizza_page_actions import (
    click_to_add_to_cart, find_add_pizza_notification, get_pizza_title, get_pizza_notification_text,
    send_keys_to_input_form
)
from src.utils.get_pizza_slider_info import get_all_possible_links


class TestAddPizzaToCartNotification:

    @allure.title("Проверка появления уведомления о добавлении пиццы в корзину")
    def test_notification_appearance(self, get_driver):
        url = choice(get_all_possible_links())
        driver = get_driver
        driver.get(url)

        click_to_add_to_cart(driver)

        assert find_add_pizza_notification(driver)

    @allure.title("Верное название пиццы в уведомлении о добавлении пиццы")
    def test_pizza_name_at_notification(self, pizza_page):
        driver = pizza_page

        pizza_name = get_pizza_title(driver, replace_quotes=False)
        click_to_add_to_cart(driver)

        assert pizza_name in get_pizza_notification_text(driver)

    @allure.title("Верное количество добавленных пицц в уведомлении о добавлении пиццы")
    def test_pizza_count_at_notification(self, pizza_page):
        driver = pizza_page
        increase_value = str(randint(2, 30))

        send_keys_to_input_form(driver=driver,
                                key=increase_value)
        click_to_add_to_cart(driver)

        assert increase_value + " ×" in get_pizza_notification_text(driver)
