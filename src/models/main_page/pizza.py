from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement


@dataclass
class Pizza:
    name: str
    price: str
    web_element: WebElement
