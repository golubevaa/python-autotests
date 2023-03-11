import allure
from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def get_driver(pytestconfig, request):
    browser = request.config.getoption("--browser")
    selenium = pytestconfig.getini("selenium_url")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
    else:
        options = webdriver.FirefoxOptions()

    with allure.step(f"Запуск браузера: {browser}"):

        driver = webdriver.Remote(
            command_executor=selenium,
            options=options)

        driver.set_window_size(1024, 600)
        driver.maximize_window()
    yield driver
    driver.quit()
