import requests
from lxml import html

from src.data.site_links import MAIN_PAGE_URL

xpath_slider = '//*[@id="accesspress_store_product-5"]'
xpath_pizzas_in_slider = ".//a/h3"


def get_pizza_slider():
    headers = {'Accept-Encoding': 'identity'}
    response = requests.get(MAIN_PAGE_URL, headers=headers)
    tree = html.fromstring(response.content)
    return tree.xpath(xpath_slider)[0]


def get_pizza_names_and_links():
    slider = get_pizza_slider()
    return [element.getparent().attrib for element in slider.xpath(xpath_pizzas_in_slider)]


def get_all_possible_names():
    return [pizza["title"] for pizza in get_pizza_names_and_links()]


def get_all_possible_links():
    return [pizza["href"] for pizza in get_pizza_names_and_links()]
