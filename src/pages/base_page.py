import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=5)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @staticmethod
    def _find(web_element, locator):
        return web_element.find_element(*locator)

    @staticmethod
    def _find_all(web_element, locator):
        return web_element.find_elements(*locator)

    def _hover(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def open(self, url):
        with allure.step(f"Открытие страницы: {url}"):
            self.driver.get(url)

    def title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def text(self, locator):
        return self.find_element(locator).text

    def click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def wait_for_presence(self, locator):
        return self.wait.until(
            ec.presence_of_element_located(locator)
        )

    def find_proposed(self, locator, element: None):
        try:
            if element:
                return self._find(element, locator)
            else:
                return self.find_element(locator)
        except NoSuchElementException:
            return None

    def get_select(self, locator):
        return Select(self.find_element(locator))

    def send_keys_to_input(self, locator, key, element: None):
        if element:
            form = self._find(web_element=element, locator=locator)
        else:
            form = self.find_element(locator)
        form.clear()
        form.send_keys(key)
        self.driver.execute_script("document.activeElement.blur();")
        return self.find_element(locator) if not element else self._find(element, locator)
