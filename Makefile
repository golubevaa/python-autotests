PYTHONPATH=$(CURDIR)

.PHONY: all_tests

all_tests:
	pytest --alluredir=./allure-results


.PHONY: cart_tests

cart_tests:
	pytest --alluredir=./allure-results tests/cart_page

.PHONY: pizza_tests

pizza_tests:
	pytest --alluredir=./allure-results tests/pizza_page

.PHONY: main_tests

main_tests:
	pytest --alluredir=./allure-results tests/main_page


