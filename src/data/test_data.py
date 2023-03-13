from random import randint

from src.utils.get_pizza_slider_info import get_all_possible_names, get_all_possible_links

# Additional options
ADD_BORTS = ["Сырный", "Колбасный"]
ALL_BORTS = ["Обычный", "Сырный", "Колбасный"]

# All pizza names
ALL_PIZZA_NAMES = get_all_possible_names()

# All pizza links
ALL_PIZZA_LINKS = get_all_possible_links()

# Sample of int values to add several products to cart
INT_SAMPLE = [randint(1, 30) for _ in range(3)]

# Factor in pizza page notification
NOTIFICATION_FACTOR = " ×"
