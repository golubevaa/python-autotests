from src.actions.common_actions import go_to_cart_via_menu
from src.actions.pizza_page_actions.pizza_page_actions import click_to_add_to_cart
from src.models.cart_page.cart import CartTable
from src.waits.common_waits import wait_for_cart_info_changes


def add_to_cart_and_wait_for_changes(driver):
    click_to_add_to_cart(driver)
    wait_for_cart_info_changes(driver=driver,
                               prev_cart_info=0)


def add_to_cart_and_get_content(driver):
    add_to_cart_and_wait_for_changes(driver)
    go_to_cart_via_menu(driver)
    cart = CartTable(driver)
    return cart
