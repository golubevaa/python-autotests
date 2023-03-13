import allure

from src.data.site_links import MAIN_PAGE_URL
from src.locators.pizza_page_locators import PizzaPageLocators
from src.models.main_page.slider import PizzaSlider
from src.pages.top_menu import PageWithTopMenu
from src.utils.to_str import rebuild_name_to_cart_page_format
from selenium.webdriver.support import expected_conditions as ec


class MainPage(PageWithTopMenu):

    def __init__(self, driver):

        super().__init__(driver, MAIN_PAGE_URL)
        self.slider = PizzaSlider(driver)

    @allure.step("Прокрутка слайдера до нужной пиццы")
    def slick_slider_until_pizza_will_be_displayed(self, pizza_name):
        while pizza_name.lower() not in self.slider.get_names():
            self.slider.slick_next()

    def move_to_button(self, button):
        self._hover(button)

    @allure.step("Добавление пиццы в корзину")
    def add_to_cart(self, product):
        self.slider.get_add_to_cart_button(product=product).click()
        self.wait_for_cart_info_changes()

    def add_pizza_from_slider_to_cart(self, pizza, pizza_in_cart):
        self.add_to_cart(pizza)
        pizza_in_cart.append(rebuild_name_to_cart_page_format(pizza))
        total_cost = self.get_cart_text()
        return pizza_in_cart, total_cost

    def open_pizza_page(self, name):
        self.slider.get_pizza_by_name(name).web_element.click()
        self.wait_for_presence(PizzaPageLocators.id_primary_content)
        return self.get_url()
