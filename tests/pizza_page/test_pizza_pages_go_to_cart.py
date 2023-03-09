import os
from src.actions.common_actions import go_to_cart_using_cart_contents, go_to_cart_via_menu
from src.actions.pizza_page_actions.pizza_page_actions import go_to_cart_via_notification
from src.helpers.get_cart_content_after_adding_pizza import add_to_cart_and_wait_for_changes


class TestPizzaPagesGoToCart:

    def test_go_to_cart_using_cart_label(self, pizza_page):
        driver = pizza_page
        go_to_cart_using_cart_contents(driver)

        assert driver.current_url == os.getenv("cart_page_url")

    def test_go_to_cart_using_head_button(self, pizza_page):
        driver = pizza_page

        go_to_cart_via_menu(driver)

        assert driver.current_url == os.getenv("cart_page_url")

    def test_go_to_cart_using_notification(self, pizza_page):
        driver = pizza_page

        add_to_cart_and_wait_for_changes(driver)
        go_to_cart_via_notification(driver)

        assert driver.current_url == os.getenv("cart_page_url")