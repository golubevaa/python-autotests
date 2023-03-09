from dataclasses import dataclass

from selenium.webdriver.remote.webelement import WebElement


@dataclass
class CartRow:
    name: str
    additional_option: str
    price: float
    amount: int
    subtotal: float
    web_element: WebElement
