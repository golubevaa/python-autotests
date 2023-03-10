from selenium.webdriver.common.by import By

from src.locators.main_page_locators import MainPageLocators
from src.waits.main_page_waits import wait_for_pizza_objects, wait_for_slider_changes


class PizzaSlider:

    def __init__(self, driver):
        self.driver = driver
        self.slider = driver.find_element(By.ID, MainPageLocators.slider_id)
        self.visible_pizzas = wait_for_pizza_objects(driver)
        self.next_slick = self.slider.find_element(By.CLASS_NAME, MainPageLocators.class_slider_slick_next)
        self.prev_slick = self.slider.find_element(By.CLASS_NAME, MainPageLocators.class_slider_slick_prev)

    def slick_next(self):
        self.next_slick.click()
        wait_for_slider_changes(self.driver, self.visible_pizzas)
        self.visible_pizzas = wait_for_pizza_objects(self.driver)

    def slick_prev(self):
        self.prev_slick.click()
        wait_for_slider_changes(self.driver, self.visible_pizzas)
        self.visible_pizzas = wait_for_pizza_objects(self.driver)

    def get_names(self):
        return [pizza.name for pizza in self.visible_pizzas]

    def get_by_name(self, name):
        return [pizza for pizza in self.visible_pizzas if pizza.name == name][0]
