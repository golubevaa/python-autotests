from selenium.webdriver.common.by import By
from src.waits.cart_page_waits import wait_for_loading_cart
from src.utils.to_float import str_to_float
import re


def get_cart_text(driver):
    cart_text = driver.find_element(By.CSS_SELECTOR, "a.cart-contents").text
    result = re.sub(r'[^0-9,]', '', cart_text)
    return str_to_float(result)


def go_to_cart_via_menu(driver):
    driver.find_element(By.ID, "menu-item-29").click()
    wait_for_loading_cart(driver)


def go_to_cart_using_cart_contents(driver):
    driver.find_element(By.CSS_SELECTOR, "a.cart-contents").click()
    wait_for_loading_cart(driver)
