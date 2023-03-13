import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.locators.main_page_locators import MainPageLocators
from src.utils.to_str import rebuild_name_to_cart_page_format


# def get_add_to_cart_button(product):
#     return product.find_element(By.XPATH, MainPageLocators.cart_button)


# def add_product_to_cart(product):
#     get_add_to_cart_button(product).click()
#
#
# def move_to_add_to_cart(product):
#     with allure.step("Наведение курсора на кнопку 'в корзину'"):
#         button = get_add_to_cart_button(product)
#         ActionChains(product.parent).move_to_element(button).perform()
#
#
# # def add_pizza_from_slider_to_cart(pizza, pizza_in_cart):
# #     with allure.step(f"Добавление пиццы '{pizza}' в корзину"):
# #         total_cost = 0
# #         add_product_to_cart(pizza.web_element)
# #         pizza_in_cart.append(rebuild_name_to_cart_page_format(pizza.name))
# #         total_cost += pizza.price
# #         return pizza_in_cart, total_cost
#
#
# def slick_slider_until_pizza_will_be_displayed(slider, pizza_name):
#     with allure.step("Прокрутка слайдера до нужной пиццы"):
#         while pizza_name.lower() not in slider.get_names():
#             slider.slick_next()
