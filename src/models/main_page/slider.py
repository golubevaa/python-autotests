import allure

from src.locators.main_page_locators import MainPageLocators
from src.models.main_page.pizza import Pizza
from src.pages.base_page import BasePage
from src.utils.to_float import find_cost_in_title
from src.utils.to_str import find_name_in_title


class PizzaSlider(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.slider = self.find_element(MainPageLocators.slider_id)
        self.visible_pizzas = self.wait_for_pizza_objects()
        self.next_slick = self._find(self.slider, MainPageLocators.slider_slick_next)
        self.prev_slick = self._find(self.slider, MainPageLocators.slider_slick_prev)

    @allure.step("Прокрутка слайдера вправо")
    def slick_next(self):
        self.next_slick.click()
        self.wait_for_slider_changes()
        self.visible_pizzas = self.wait_for_pizza_objects()

    @allure.step("Прокрутка слайдера влево")
    def slick_prev(self):
        self.prev_slick.click()
        self.wait_for_slider_changes()
        self.visible_pizzas = self.wait_for_pizza_objects()

    @allure.step("Получение списка видимых пицц")
    def get_names(self):
        names = [pizza.name for pizza in self.visible_pizzas]
        return names

    def get_pizza_by_name(self, name):
        return [pizza for pizza in self.visible_pizzas if pizza.name == name.lower()][0]

    def wait_for_pizza_objects(self):
        return self.wait.until(lambda d: self.get_visible_pizzas())

    def wait_for_slider_changes(self):
        self.wait.until(lambda d: self.get_visible_pizzas() != self.visible_pizzas)

    def get_visible_pizzas(self):
        pizza_list = []
        visible_pizzas = {}
        while len(visible_pizzas) != 4:
            visible_pizzas = {el.text: el for el in self._find_all(self.slider, MainPageLocators.pizza)
                              if el.is_displayed() and el.text}
        for name_and_price, web_element in visible_pizzas.items():
            pizza_list.append(
                Pizza(
                    name=find_name_in_title(name_and_price),
                    price=find_cost_in_title(name_and_price),
                    web_element=web_element
                )
            )
        return pizza_list

    @allure.step("Получение кнопки 'В корзину'")
    def get_add_to_cart_button(self, product):
        pizza = self.get_pizza_by_name(product).web_element
        return self._find(pizza, MainPageLocators.cart_button)
