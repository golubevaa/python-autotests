import allure

from src.locators.cart_page_locators import CartPageLocators
from src.models.cart_page.cart_row import CartRow
from src.pages.base_page import BasePage
from src.utils.to_float import str_to_float


class CartTable(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        with allure.step("Получение контента корзины"):
            self.cart_rows = self._all_info_about_cart_products()

    def _get_additional_options(self, product_el):
        options = self.find_proposed(locator=CartPageLocators.css_add_option, element=product_el)
        if options:
            return options.text

    def _all_info_about_cart_products(self):
        products = self._get_cart_products()
        result = list(map(self._parse_product_options, products))
        return result

    def _get_cart_products(self):
        return self.find_elements(CartPageLocators.css_cart_product_table)

    def _parse_product_options(self, product_el):
        return CartRow(
            name=self._find(product_el, CartPageLocators.class_name_of_product).text,
            additional_option=self._get_additional_options(product_el),
            price=str_to_float(self._find(product_el, CartPageLocators.class_price_of_product).text[:-1]),
            amount=int(self._find(product_el, CartPageLocators.css_amount_input).get_attribute("value")),
            subtotal=str_to_float(self._find(product_el, CartPageLocators.class_subtotal_product).text[:-1]),
            web_element=product_el
        )

    def update(self):
        self.cart_rows = self._all_info_about_cart_products()

    def count_products(self):
        with allure.step("Подсчет кол-ва продуктов в корзине"):
            return sum(row.amount for row in self.cart_rows)

    def get_by_index(self, index):
        return self.cart_rows[index]

    def get_first_by_amount(self, amount):
        with allure.step(f"Получение первой пиццы, количество которой в ячейке = {amount}"):
            return [row for row in self.cart_rows if row.amount == amount][0]

    def get_first_by_add_option(self, add_option):
        with allure.step(f"Получение перовго элемента с доп. опцией = '{add_option}'"):
            return [row for row in self.cart_rows if (row.additional_option and add_option in row.additional_option)][0]

    def get_names_by_amount(self, amount):
        with allure.step(f"Получение списка названий пицц, количество которых в корзине равно {amount}"):
            return [row.name for row in self.cart_rows if row.amount == amount]

    def get_first_row_by_row_amount_greater_then(self, value):
        with allure.step(f"Получение первой пиццы, количество которой в ячейке больше {value}"):
            return [row for row in self.cart_rows if row.amount > value][0]
