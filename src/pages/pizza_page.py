import allure

from src.locators.pizza_page_locators import PizzaPageLocators
from src.pages.top_menu import PageWithTopMenu
from src.utils.to_float import str_to_float
from src.utils.to_str import rebuild_name_to_cart_page_format


class PizzaPage(PageWithTopMenu):
    def __init__(self, driver, url):

        super().__init__(driver, url)
        self.product_title = self.get_title()
        self.cart_format_product_title = rebuild_name_to_cart_page_format(self.product_title)
        self.doping_menu = self.doping_menu()

    def get_title(self):
        return self.text(PizzaPageLocators.pizza_title)

    def doping_menu(self):
        return self.get_select(PizzaPageLocators.id_doping_menu)

    def select_doping_by_name(self, name):
        with allure.step(f"Выбор допинга: {name}"):
            for option in self.doping_menu.options:
                if name in option.text:
                    self.doping_menu.select_by_visible_text(option.text)
                    return

    @allure.step("Получение цены допинга")
    def get_doping_price(self, name):
        for option in self.doping_menu.options:
            if name in option.text:
                return float(option.get_attribute("value"))

    def send_keys_to_input_form(self, key):
        input_form = self.send_keys_to_input(locator=PizzaPageLocators.amount_input,
                                             key=key,
                                             element=None)
        if input_form:
            return input_form.get_attribute("value")

    def add_to_cart(self):
        self.click(PizzaPageLocators.add_to_cart_button)
        self.wait_for_cart_info_changes()

    @allure.step("Получение списка дополнительных опций")
    def get_options_text(self):
        result = [option.text if "-" not in option.text else option.text.split(" - ")[0]
                  for option in self.doping_menu.options]
        return result

    @allure.step("получение цены пиццы")
    def get_price(self):
        price = self.text(PizzaPageLocators.pizza_price)[:-1]
        return str_to_float(price)

    @allure.step("Поиск уведомления о добавлении пиццы в корзину")
    def find_notification(self):
        return self.find_proposed(locator=PizzaPageLocators.add_to_cart_notification, element=None)

    @allure.step("Переход в корзину через уведомление о добавлении пиццы")
    def go_to_cart_via_notification(self):
        notification = self.find_notification()
        url = self._find(notification, PizzaPageLocators.go_to_cart_from_notification).get_attribute("href")
        self.open(url)
