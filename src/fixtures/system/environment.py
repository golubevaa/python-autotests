import pytest
import os


@pytest.fixture(autouse=True, scope="session")
def environment(pytestconfig, request):
    os.environ["main_page_url"] = pytestconfig.getini("main_page_url")
    os.environ["cart_page_url"] = pytestconfig.getini("cart_page_url")
    os.environ["selenium_url"] = pytestconfig.getini("selenium_url")

    def remove_env_vars():
        for name in ["main_page_url", "cart_page_url", "selenium_url"]:
            os.unsetenv(name)

    yield

    request.addfinalizer(remove_env_vars)
