from selenium.webdriver.support.wait import WebDriverWait
from src.actions.main_page_actions.get_pizzas import get_visible_pizzas


def wait_for_pizza_objects(driver):
    return WebDriverWait(driver, timeout=3).until(lambda d: get_visible_pizzas(d))


def wait_for_slider_changes(driver, prev_pizzas):
    WebDriverWait(driver, timeout=3).until(
        lambda d: get_visible_pizzas(d) != prev_pizzas)
