from selenium.webdriver.common.by import By


class CartPageLocators:

    content_table = (By.CLASS_NAME, "content-page")
    cart_page_update_marker = (By.CSS_SELECTOR, ".blockUI.blockOverlay")
    css_cart_product_table = (By.CSS_SELECTOR, "tr.cart_item")
    class_name_of_product = (By.CLASS_NAME, "product-name")
    class_price_of_product = (By.CLASS_NAME, "product-price")
    css_amount_input = (By.CSS_SELECTOR, "input.input-text")
    class_subtotal_product = (By.CLASS_NAME, "product-subtotal")
    css_add_option = (By.CSS_SELECTOR, "dd.variation-")
    tag_pizza_amount = (By.TAG_NAME, "input")
    name_update_cart_button = (By.NAME, "update_cart")
    class_empty_cart_message = (By.CLASS_NAME, "cart-empty")
    class_remove_button = (By.CLASS_NAME, "remove")
