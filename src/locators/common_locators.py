from selenium.webdriver.common.by import By


class CommonLocators:

    # Locators are the same for all pages

    cart_locator = (By.CSS_SELECTOR, "a.cart-contents")
    id_cart_button = (By.ID, "menu-item-29")
