from src.actions.cart_page_actions.cart_page_actions import all_info_about_cart_products


class CartTable:

    def __init__(self, driver):
        self.driver = driver
        self.cart_rows = all_info_about_cart_products(driver)

    def update(self):
        self.cart_rows = all_info_about_cart_products(self.driver)

    def count_products(self):
        return sum(row.amount for row in self.cart_rows)

    def get_by_index(self, index):
        return self.cart_rows[index].name

    def get_first_by_amount(self, amount):
        return [row for row in self.cart_rows if row.amount == amount][0]

    def get_first_by_add_option(self, add_option):
        return [row for row in self.cart_rows if (row.additional_option and add_option in row.additional_option)][0]

    def get_names_by_amount(self, amount):
        return [row.name for row in self.cart_rows if row.amount == amount]

    def get_first_row_by_row_amount_greater_then(self, value):
        return [row for row in self.cart_rows if row.amount > value][0]
