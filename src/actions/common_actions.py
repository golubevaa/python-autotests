from selenium.webdriver.common.by import By
import allure

from src.locators.common_locators import CommonLocators
from src.waits.cart_page_waits import wait_for_loading_cart
from src.utils.to_float import str_to_float
import re


def get_cart_text(driver):
    cart_text = driver.find_element(By.CSS_SELECTOR, CommonLocators.cart_locator).text
    result = re.sub(r'[^0-9,]', '', cart_text)
    return str_to_float(result)


def go_to_cart_via_menu(driver):
    with allure.step("Переход в корзину с помощью общего меню"):
        driver.find_element(By.ID, CommonLocators.id_cart_button).click()
        wait_for_loading_cart(driver)


def go_to_cart_using_cart_contents(driver):
    with allure.step("Переход в корзину через значок корзины"):
        driver.find_element(By.CSS_SELECTOR, CommonLocators.cart_locator).click()
        wait_for_loading_cart(driver)
