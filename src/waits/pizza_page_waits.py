from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from src.locators.pizza_page_locators import PizzaPageLocators


def wait_for_loading_pizza_page(driver):
    WebDriverWait(driver, timeout=3).until(
        ec.presence_of_element_located((By.ID, PizzaPageLocators.id_primary_content))
    )
