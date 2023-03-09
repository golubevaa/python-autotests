from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_loading_cart(driver):
    WebDriverWait(driver, timeout=3).until(ec.presence_of_element_located((By.CLASS_NAME, "content-page")))
