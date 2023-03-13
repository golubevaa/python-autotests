import allure

from src.locators.pizza_page_locators import PizzaPageLocators
from src.pages.top_menu import PageWithTopMenu
from src.utils.to_float import str_to_float
from src.utils.to_str import rebuild_name_to_cart_page_format


class PizzaPage(PageWithTopMenu):
    def __init__(self, driver, url):

        super().__init__(driver, url)
        self.product_title = self.get_title()
        self.doping_menu = self.doping_menu()

    def get_title(self):
        return self.text(PizzaPageLocators.pizza_title).lower()

    def doping_menu(self):
        return self.get_select(PizzaPageLocators.id_doping_menu)

    def select_doping_by_name(self, name):
        with allure.step(f"Выбор допинга: {name}"):
            for option in self.doping_menu.options:
                if name in option.text:
                    self.doping_menu.select_by_visible_text(option.text)
                    return

    @allure.step(f"Получение цены допинга")
    def get_doping_price(self, name):
        for option in self.doping_menu.options:
            if name in option.text:
                return float(option.get_attribute("value"))

    def send_keys_to_input_form(self, key):
        return self.send_keys_to_input(locator=PizzaPageLocators.amount_input, key=key)

    def add_to_cart(self):
        self.find_element(PizzaPageLocators.add_to_cart_button).click()
        self.wait_for_cart_info_changes()

    @allure.step("Получение списка дополнительных опций")
    def get_options_text(self):
        result = [option.text if "-" not in option.text else option.text.split(" - ")[0]
                  for option in self.doping_menu()]
        return result

    @allure.step("получение цены пиццы")
    def get_price(self):
        price = self.text(PizzaPageLocators.pizza_price)[:-1]
        return str_to_float(price)

    @allure.step("Поиск уведомления о добавлении пиццы в корзину")
    def find_notification(self):
        return self.find_proposed(PizzaPageLocators.add_to_cart_notification)

    def add_to_cart_and_get_content(self):
        self.add_to_cart()
        self.go_to_cart_via_menu()



