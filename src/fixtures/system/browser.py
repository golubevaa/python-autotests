from selenium.webdriver import Remote
import pytest


@pytest.fixture()
def get_driver(pytestconfig):
    selenium_hub = pytestconfig.getini("selenium_url")
    driver = Remote(desired_capabilities={
        "browserName": "chrome",
        "selenoid:options": {
            "enableVnc": True
        },
    }, command_executor=selenium_hub)
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    yield driver
    driver.quit()
