from re import sub

import allure

from src.locators.common_locators import CommonLocators
from src.pages.base_page import BasePage
from src.utils.to_float import str_to_float


class PageWithTopMenu(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver)
        if self.get_url() != url:
            self.open(url)
        self._cart_text = self.get_cart_text()

    @allure.step("Получение стоимости добавленных продуктов в корзине (топ бар)")
    @property
    def cart_text(self):
        return self._cart_text

    def get_cart_text(self):
        cart_text = self.find_element(CommonLocators.cart_locator).text
        result = sub(r'[^0-9,]', '', cart_text)
        return str_to_float(result)

    @allure.step("Переход в корзину с помощью общего меню")
    def go_to_cart_via_menu(self):
        self.find_element(CommonLocators.id_cart_button).click()

    def wait_for_cart_info_changes(self):
        self.wait.until(
            lambda d: self._cart_text != self.get_cart_text()
        )
        self._cart_text = self.get_cart_text()

    @allure.step("Переход в корзину через значок корзины")
    def go_to_cart_using_cart_contents(self):
        self.find_element(CommonLocators.cart_locator).click()

