from selenium.webdriver.common.by import By

from src.locators.main_page_locators import MainPageLocators
from src.models.main_page.pizza import Pizza
from src.utils.to_str import find_name_in_title
from src.utils.to_float import find_cost_in_title


def get_visible_pizzas(driver):
    pizza_list = []
    slider = driver.find_element(By.ID, MainPageLocators.slider_id)
    visible_pizzas = {}
    while len(visible_pizzas) != 4:
        visible_pizzas = {el.text: el for el in slider.find_elements(By.TAG_NAME, MainPageLocators.pizza_element_tag)
                          if el.is_displayed() and el.text}
    for name_and_price, web_element in visible_pizzas.items():
        pizza_list.append(Pizza(name=find_name_in_title(name_and_price),
                                price=find_cost_in_title(name_and_price),
                                web_element=web_element,))
    return pizza_list
