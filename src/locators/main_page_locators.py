from selenium.webdriver.common.by import By


class MainPageLocators:

    cart_button = (By.XPATH, ".//*[contains(text(), 'В корзину')]")
    slider_id = (By.ID, "accesspress_store_product-5")
    slider_slick_next = (By.CLASS_NAME, "slick-next")
    slider_slick_prev = (By.CLASS_NAME, "slick-prev")
    pizza = (By.TAG_NAME, "li")
