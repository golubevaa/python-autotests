import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from src.locators.pizza_page_locators import PizzaPageLocators
from src.utils.to_float import str_to_float
from src.waits.cart_page_waits import wait_for_loading_cart
from src.utils.to_str import rebuild_name_to_cart_page_format


def open_pizza_page(pizza_element):
    with allure.step("Открытие страницы пиццы"):
        pizza_element.click()


def get_pizza_title(driver, replace_quotes=True):
    with allure.step("Получение названия пиццы"):
        title = driver.find_element(By.CLASS_NAME, PizzaPageLocators.pizza_title).text.lower()
        return rebuild_name_to_cart_page_format(title) if replace_quotes else title


def get_pizza_price(driver):
    with allure.step("получение цены пиццы"):
        price = driver.find_element(By.CSS_SELECTOR, PizzaPageLocators.pizza_price).text[:-1]
        return str_to_float(price)


def find_doping_menu(driver):
    return Select(driver.find_element(By.ID, PizzaPageLocators.id_doping_menu))


def get_doping_price(menu, name):
    with allure.step(f"Получение цены допинга: {name}"):
        for option in menu.options:
            if name in option.text:
                return float(option.get_attribute("value"))


def get_doping_options_text(driver, without_cost):
    with allure.step("Получение списка дополнительных опций"):
        if without_cost:
            result = [option.text if "-" not in option.text else option.text.split(" - ")[0]
                      for option in find_doping_menu(driver).options]
        else:
            result = [option.text for option in find_doping_menu(driver).options]
        return result


def select_doping_by_name(menu, name):
    with allure.step(f"Выбор допинга: {name}"):
        for option in menu.options:
            if name in option.text:
                menu.select_by_visible_text(option.text)
                return


def send_keys_to_input_form(driver, key):
    with allure.step(f"Изменение кол-ва пицц в инпут форме: {key}"):
        counter = driver.find_element(By.CSS_SELECTOR, PizzaPageLocators.amount_input)
        counter.clear()
        counter.send_keys(key)
        return driver.find_element(By.CSS_SELECTOR, PizzaPageLocators.amount_input)


def click_to_add_to_cart(driver):
    with allure.step("Нажатие на кнопку 'добавить в корзину'"):
        driver.find_element(By.CSS_SELECTOR, PizzaPageLocators.add_to_cart_button).click()


def get_add_pizza_notification(driver):
    with allure.step("Поиск уведомления о добавлении пиццы в корзину на странице"):
        return driver.find_element(By.CLASS_NAME, PizzaPageLocators.add_to_cart_notification)


def find_add_pizza_notification(driver):
    try:
        get_add_pizza_notification(driver)
        return True
    except NoSuchElementException:
        return False


def get_pizza_notification_text(driver):
    with allure.step("Получение текста уведомления о добавлении пиццы в корзину"):
        return get_add_pizza_notification(driver).text.lower()


def go_to_cart_via_notification(driver):
    with allure.step("Переход в корзину через уведомление о добавлении пиццы"):
        notification = get_add_pizza_notification(driver)
        notification.find_element(By.CLASS_NAME, PizzaPageLocators.go_to_cart_from_notification).click()
        wait_for_loading_cart(driver)
