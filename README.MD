# Тестовый репозитой - Pytest + Selenium Grid

## Тесты для сайта http://pizzeria.skillbox.cc/

Демо репозиторий. \
Есть пайплайн в actions. \
Результаты запусков: https://golubevaa.github.io/python-autotests/

### Подготовка

Требуется установленный докер.
Проектные зависимости в файлах environment.yml (использую conda) или requirements.txt.

### Запуск тестов

Для локального запуска подготовила makefile с возможностью запуска всего проекта или отдельных тестов.
Команды:
* all_tests - все тесты
* cart_tests - тесты на корзину
* pizza_tests - тесты на страницах пицц
* main_tests - тесты главной страницы
* only_sanity - тесты с маркером sanity
* only_high_priority - тесты с маркером high_priority

При желании запустить отдельные тесты потребуется запустить docker контейнеры с selenium.
```
docker compose up -d 
```


### Планы

* Добавить логирование
* Переписать asserts на pyhamcrest
* Написать больше тестов :)
