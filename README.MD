# Тестовый репозитой - Pytest + Selenium (Selenoid)

## Тесты для сайта http://pizzeria.skillbox.cc/

Репозиторий находится в разработке. Выложен с целью показать примеры тестов. 

### Подготовка

Запускаю с помощью docker контейнера с Selenoid. \
Configuration manager: https://github.com/aerokube/cm/releases 

Запуск Selenoid
```
chmod +x cm
./cm selenoid start --vnc
```
Если требуется Selenoid UI (будет доступен на порте 8080):
```
./cm selenoid-ui start
```

Проектные зависимости в файлах environment.yml (использую conda) или requirements.txt.

### Запуск тестов

Для запуска подготовила makefile с возможностью запуска всего проекта (make all_tests) или отдельных папок (cart_tests, main_tests  и т.д). \
Запуск из корневой директории проекта.

### Планы

* Добавить allure репорты (пока только тайтлы у тестов)
* Добавить логирование
* Переписать asserts на pyhamcrest
* Допилить тесты :)
* Сделать запуски на разных браузерах
