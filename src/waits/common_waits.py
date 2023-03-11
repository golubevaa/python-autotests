import allure
from selenium.webdriver.support.wait import WebDriverWait
from src.actions.common_actions import get_cart_text


def wait_for_cart_info_changes(driver, prev_cart_info):
    WebDriverWait(driver, timeout=3).until(
        lambda d: prev_cart_info != get_cart_text(d)
    )
