from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from src.locators.pizza_page_locators import PizzaPageLocators
from src.utils.to_float import str_to_float
from src.waits.cart_page_waits import wait_for_loading_cart
from re import sub


def open_pizza_page(pizza_element):
    pizza_element.click()


def get_pizza_title(driver, replace_quotes=True):
    title = driver.find_element(By.CLASS_NAME, PizzaPageLocators.class_pizza_title).text.lower()
    return sub(r'[«»]', '"', title) if replace_quotes else title


def get_pizza_price(driver):
    price = driver.find_element(By.CSS_SELECTOR, PizzaPageLocators.css_pizza_price).text[:-1]
    return str_to_float(price)


def find_doping_menu(driver):
    return Select(driver.find_element(By.ID, PizzaPageLocators.id_doping_menu))


def get_doping_price(menu, name):
    for option in menu.options:
        if name in option.text:
            return float(option.get_attribute("value"))


def get_doping_options_text(driver, without_cost):
    if without_cost:
        result = [option.text if "-" not in option.text else option.text.split(" - ")[0]
                  for option in find_doping_menu(driver).options]
    else:
        result = [option.text for option in find_doping_menu(driver).options]
    return result


def select_doping_by_name(menu, name):
    for option in menu.options:
        if name in option.text:
            menu.select_by_visible_text(option.text)
            return


def send_keys_to_input_form(driver, key):
    counter = driver.find_element(By.CSS_SELECTOR, PizzaPageLocators.css_amount_input)
    counter.clear()
    counter.send_keys(key)
    return driver.find_element(By.CSS_SELECTOR, PizzaPageLocators.css_amount_input)


def click_to_add_to_cart(driver):
    driver.find_element(By.CSS_SELECTOR, PizzaPageLocators.css_add_to_cart_button).click()


def get_add_pizza_notification(driver):
    return driver.find_element(By.CLASS_NAME, PizzaPageLocators.class_add_to_cart_notification)


def find_add_pizza_notification(driver):
    try:
        get_add_pizza_notification(driver)
        return True
    except NoSuchElementException:
        return False


def get_pizza_notification_text(driver):
    return get_add_pizza_notification(driver).text.lower()


def go_to_cart_via_notification(driver):
    notification = get_add_pizza_notification(driver)
    notification.find_element(By.CLASS_NAME, PizzaPageLocators.class_go_to_cart_from_notification).click()
    wait_for_loading_cart(driver)
