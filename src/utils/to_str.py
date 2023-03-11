from re import sub

def convert_cost_to_prod_format(float_cost):
    return str(float_cost).replace(".", ",")


def find_name_in_title(title):
    return title.split("\n")[0].lower()


def rebuild_name_to_cart_page_format(name):
    return sub(r'[«»]', '"', name)

