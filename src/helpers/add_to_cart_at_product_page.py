import allure

from src.pages.pizza_page import PizzaPage


def go_to_pizza_page_and_add_to_cart(driver, param):
    pizza_page = PizzaPage(driver, param.url)
    pizza_page.select_doping_by_name(param.options.bort)
    pizza_page.send_keys_to_input_form(param.options.value)
    pizza_page.add_to_cart()
