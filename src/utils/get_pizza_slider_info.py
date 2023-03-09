import requests
from lxml import html


def get_pizza_slider():
    headers = {'Accept-Encoding': 'identity'}
    response = requests.get('http://pizzeria.skillbox.cc/', headers=headers)
    tree = html.fromstring(response.content)
    return tree.xpath('//*[@id="accesspress_store_product-5"]')[0]


def get_pizza_names_and_links():
    slider = get_pizza_slider()
    return [element.getparent().attrib for element in slider.xpath(".//a/h3")]


def get_all_possible_names():
    return [pizza["title"] for pizza in get_pizza_names_and_links()]


def get_all_possible_links():
    return [pizza["href"] for pizza in get_pizza_names_and_links()]
