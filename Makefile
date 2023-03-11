.PHONY: dc-up

dc-up:
	docker compose up -d


.PHONY: all_tests

all_tests: dc-up
	pytest --browser=firefox --alluredir=./allure-results
	docker compose down

.PHONY: cart_tests

cart_tests: dc-up
	pytest --alluredir=./allure-results tests/cart_page
	docker compose down

.PHONY: pizza_tests

pizza_tests: dc-up
	pytest --alluredir=./allure-results tests/pizza_page
	docker compose down
.PHONY: main_tests

main_tests: dc-up
	pytest --alluredir=./allure-results tests/main_page
	docker compose down

.PHONY: only_sanity

only_sanity: dc-up
	pytest --alluredir=./allure-results tests/main_page -m sanity
	docker compose down

.PHONY: only_high_priority

only_high_priority: dc-up
	pytest --alluredir=./allure-results tests/main_page -m high_priority
	docker compose down


