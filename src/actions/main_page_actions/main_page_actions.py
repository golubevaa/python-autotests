from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from re import sub


def get_add_to_cart_button(product):
    return product.find_element(By.XPATH, ".//*[contains(text(), 'В корзину')]")


def add_product_to_cart(product):
    get_add_to_cart_button(product).click()


def move_to_add_to_cart(product):
    button = get_add_to_cart_button(product)
    ActionChains(product.parent).move_to_element(button).perform()


def add_pizza_from_slider_to_cart(pizza_list, pizza_in_cart):
    total_cost = 0
    for pizza in pizza_list:
        add_product_to_cart(pizza.web_element)
        pizza_in_cart.append(sub(r'[«»]', '"', pizza.name))
        total_cost += pizza.price
    return pizza_in_cart, total_cost


def slick_slider_until_pizza_will_be_displayed(slider, pizza_name):
    while pizza_name not in slider.get_names():
        slider.slick_next()
