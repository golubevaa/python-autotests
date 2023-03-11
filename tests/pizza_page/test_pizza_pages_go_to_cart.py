import allure

from src.actions.common_actions import go_to_cart_using_cart_contents, go_to_cart_via_menu
from src.actions.pizza_page_actions.pizza_page_actions import go_to_cart_via_notification
from src.data.site_links import CART_PAGE_URL
from src.helpers.get_cart_content_after_adding_pizza import add_to_cart_and_wait_for_changes


@allure.feature("Страницы пицц")
@allure.story("Переход в корзину")
class TestPizzaPagesGoToCart:

    @allure.title("Переход в корзину с помощью значка корзины")
    def test_go_to_cart_using_cart_label(self, pizza_page):
        driver = pizza_page
        go_to_cart_using_cart_contents(driver)

        assert driver.current_url == CART_PAGE_URL

    @allure.title("Переход в корзину с помощью общего меню")
    def test_go_to_cart_using_head_button(self, pizza_page):
        driver = pizza_page

        go_to_cart_via_menu(driver)

        assert driver.current_url == CART_PAGE_URL

    @allure.title("Переход в корзину с помощью уведомления о добавлении пиццы")
    def test_go_to_cart_using_notification(self, pizza_page):
        driver = pizza_page

        add_to_cart_and_wait_for_changes(driver)
        go_to_cart_via_notification(driver)

        assert driver.current_url == CART_PAGE_URL
        