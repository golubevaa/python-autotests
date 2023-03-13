from src.data.site_links import CART_PAGE_URL
from src.locators.cart_page_locators import CartPageLocators
from src.models.cart_page.cart import CartTable

from src.pages.top_menu import PageWithTopMenu


class CartPage(PageWithTopMenu):

    def __init__(self, driver):
        super().__init__(driver, CART_PAGE_URL)
        self.cart = CartTable(self.driver)

    def wait_for_loading(self):
        self.wait_for_presence(CartPageLocators.content_table)

