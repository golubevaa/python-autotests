import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.locators.cart_page_locators import CartPageLocators
from src.utils.to_float import str_to_float
from src.models.cart_page.cart_row import CartRow
from src.waits.cart_page_waits import wait_for_updating_cart


def get_cart_products(driver):
    return driver.find_elements(By.CSS_SELECTOR, CartPageLocators.css_cart_product_table)


def get_name(product_el):
    return product_el.find_element(By.CLASS_NAME, CartPageLocators.class_name_of_product).text


def get_price(product_el):
    return str_to_float(product_el.find_element(By.CLASS_NAME, CartPageLocators.class_price_of_product).text[:-1])


def get_amount(product_el):
    return int(product_el.find_element(By.CSS_SELECTOR, CartPageLocators.css_amount_input).get_attribute("value"))


def get_subtotal_cost(product_el):
    return str_to_float(product_el.find_element(By.CLASS_NAME, CartPageLocators.class_subtotal_product).text[:-1])


def get_additional_options(product_el):
    try:
        return product_el.find_element(By.CSS_SELECTOR, CartPageLocators.css_add_option).text
    except NoSuchElementException:
        return None


def parse_product_options(product_el: WebElement):
    return CartRow(
            name=get_name(product_el),
            additional_option=get_additional_options(product_el),
            price=get_price(product_el),
            amount=get_amount(product_el),
            subtotal=get_subtotal_cost(product_el),
            web_element=product_el
    )


def all_info_about_cart_products(driver):
    result = []
    products = get_cart_products(driver)
    for i in range(len(products)):
        result.append(parse_product_options(products[i]))
    return result


def send_keys_to_number_of_pizza_form(pizza_row, key):
    with allure.step(f"Изменение кол-ва пицц в ячейке. Новое значение: {key}"):
        _input = pizza_row.find_element(By.TAG_NAME, CartPageLocators.tag_pizza_amount)
        _input.clear()
        _input.send_keys(key)
        pizza_row.parent.execute_script("document.activeElement.blur();")


def get_update_cart_button(driver):
    with allure.step("Получение кнопки обновления корзины"):
        return driver.find_element(By.NAME, CartPageLocators.name_update_cart_button)


def click_to_update_cart_button(driver):
    with allure.step("Обновление содержимого корзины с помощью кнопки обновления"):
        get_update_cart_button(driver).click()
        wait_for_updating_cart(driver)


def find_empty_cart_message(driver):
    return driver.find_element(By.CLASS_NAME, CartPageLocators.class_empty_cart_message)


@allure.step("Проверка что корзина пустая")
def cart_is_empty(driver):
    try:
        find_empty_cart_message(driver)
        return True
    except NoSuchElementException:
        return False


def remove_product(product):
    product.find_element(By.CLASS_NAME, CartPageLocators.class_remove_button).click()
