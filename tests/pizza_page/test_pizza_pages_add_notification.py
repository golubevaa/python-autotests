import allure
from random import randint

from src.data.test_data import NOTIFICATION_FACTOR


@allure.feature("Страницы пицц")
@allure.story("Уведомление о добавлении пиццы в корзину")
class TestAddPizzaToCartNotification:

    @allure.title("Проверка появления уведомления о добавлении пиццы в корзину")
    def test_notification_appearance(self, pizza_page):
        pizza_page.add_to_cart()

        assert pizza_page.find_notification()

    @allure.title("Верное название пиццы в уведомлении о добавлении пиццы")
    def test_pizza_name_at_notification(self, pizza_page):
        pizza_name = pizza_page.product_title

        pizza_page.add_to_cart()

        assert pizza_name in pizza_page.find_notification().text

    @allure.title("Верное количество добавленных пицц в уведомлении о добавлении пиццы")
    def test_pizza_count_at_notification(self, pizza_page):
        increase_value = str(randint(2, 30))

        pizza_page.send_keys_to_input_form(key=increase_value)
        pizza_page.add_to_cart()

        assert increase_value + NOTIFICATION_FACTOR in pizza_page.find_notification().text
