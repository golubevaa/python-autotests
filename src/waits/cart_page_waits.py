from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from src.locators.cart_page_locators import CartPageLocators


def wait_for_loading_cart(driver):
    WebDriverWait(driver, timeout=3).until(
        ec.presence_of_element_located((By.CLASS_NAME, CartPageLocators.class_content_table))
    )


def wait_for_updating_cart(driver):
    WebDriverWait(driver, timeout=3).until(
        ec.staleness_of(driver.find_elements(By.CSS_SELECTOR, CartPageLocators.css_cart_page_update_marker)[0])
    )
