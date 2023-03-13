import allure
from src.data.site_links import CART_PAGE_URL


@allure.feature("Страницы пицц")
@allure.story("Переход в корзину")
class TestPizzaPagesGoToCart:

    @allure.title("Переход в корзину с помощью значка корзины")
    def test_go_to_cart_using_cart_label(self, pizza_page):

        pizza_page.go_to_cart_using_cart_contents()

        assert pizza_page.get_url() == CART_PAGE_URL

    @allure.title("Переход в корзину с помощью общего меню")
    def test_go_to_cart_using_head_button(self, pizza_page):

        pizza_page.go_to_cart_via_menu()

        assert pizza_page.get_url() == CART_PAGE_URL

    @allure.title("Переход в корзину с помощью уведомления о добавлении пиццы")
    def test_go_to_cart_using_notification(self, pizza_page):

        pizza_page.add_to_cart()
        pizza_page.go_to_cart_via_notification()

        assert pizza_page.get_url() == CART_PAGE_URL
