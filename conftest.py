pytest_plugins = [
    'src.fixtures'
]


def pytest_addoption(parser):
    parser.addini("selenium_url", "Selenium Hub url")
    parser.addoption("--browser", action="store", default="firefox", help="Browser type")
