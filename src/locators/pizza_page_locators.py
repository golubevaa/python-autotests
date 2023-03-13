from selenium.webdriver.common.by import By


class PizzaPageLocators:

    id_primary_content = (By.ID, "primary")
    pizza_title = (By.CLASS_NAME, "product_title")
    pizza_price = (By.CSS_SELECTOR, "p.price bdi")
    id_doping_menu = (By.ID, "board_pack")
    amount_input = (By.CSS_SELECTOR, "input[type='number']")
    add_to_cart_button = (By.CSS_SELECTOR, "button[name='add-to-cart']")
    add_to_cart_notification = (By.CLASS_NAME, "woocommerce-message")
    go_to_cart_from_notification = (By.CLASS_NAME, "wc-forward")
