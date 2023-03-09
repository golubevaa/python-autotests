pytest_plugins = [
    'src.fixtures'
]


def pytest_addoption(parser):
    parser.addini("selenium_url", "Selenium Hub url")
    parser.addini("main_page_url", "Main page url")
    parser.addini("cart_page_url", "Cart page url")
