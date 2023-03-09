from random import randint, shuffle, sample
from collections import namedtuple

from src.utils.get_pizza_slider_info import get_all_possible_links


def shuffle_pizza_props():
    urls = sample(get_all_possible_links(), k=3)
    borts = ["Обычный", "Сырный", "Колбасный"]
    values = [1, *(randint(2, 30) for _ in range(2))]
    shuffle(borts)
    shuffle(values)

    Options = namedtuple("Options", ("bort", "value"))
    options = map(lambda opt: Options(*opt), zip(borts, values))

    Params = namedtuple("Params", ("url", "options"))
    params = list(map(lambda param: Params(*param), zip(urls, options)))

    return params
