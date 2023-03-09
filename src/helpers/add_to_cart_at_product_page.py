from src.actions.pizza_page_actions.pizza_page_actions import (
    find_doping_menu, select_doping_by_name, send_keys_to_input_form
)
from src.helpers.get_cart_content_after_adding_pizza import add_to_cart_and_wait_for_changes


def go_to_pizza_page_and_add_to_cart(driver, param):
    driver.get(param.url)
    menu = find_doping_menu(driver)
    select_doping_by_name(menu=menu,
                          name=param.options.bort)
    send_keys_to_input_form(driver=driver,
                            key=param.options.value)
    add_to_cart_and_wait_for_changes(driver)
