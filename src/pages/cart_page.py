import allure

from src.data.site_links import CART_PAGE_URL
from src.locators.cart_page_locators import CartPageLocators
from src.models.cart_page.cart import CartTable
from selenium.webdriver.support import expected_conditions as ec
from src.pages.top_menu import PageWithTopMenu


class CartPage(PageWithTopMenu):

    def __init__(self, driver):
        super().__init__(driver, CART_PAGE_URL)
        self.cart = CartTable(self.driver)

    def wait_for_loading(self):
        self.wait_for_presence(CartPageLocators.content_table)

    @allure.step("Изменение кол-ва пицц в ячейке")
    def send_keys_to_pizza_form(self, key, element):
        with allure.step(f"Новое значение: {key}"):
            self.send_keys_to_input(locator=CartPageLocators.tag_pizza_amount,
                                    key=key,
                                    element=element)

    @allure.step("Клик на кнопку обновления корзины")
    def click_to_update_cart_button(self):
        self.click(CartPageLocators.name_update_cart_button)
        self.wait_for_updating()

    def wait_for_updating(self):
        self.wait.until(
            ec.staleness_of(self.find_elements(CartPageLocators.cart_page_update_marker)[0])
        )
        self.cart.update()

    def cart_is_empty(self):
        message = self.find_proposed(locator=CartPageLocators.class_empty_cart_message, element=None)
        return True if message else False
