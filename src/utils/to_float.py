def find_cost_in_title(element_name):
    cost_str = element_name.split("\n")[1][:-1]
    return str_to_float(cost_str)


def str_to_float(number):
    return float(number.replace(",", "."))
