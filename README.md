# Проект "Виджет личного кабинета клиента"

## Описание:!

Проект - виджет для личного кабинета клиента.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/DmitryPikov/my_project.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```
4. Добавлен модуль generators.py, который содержит функции для работы с массивами транзакций.
5. Добавлен модуль decorators.py, который содержит функции для вывода лога в консоль или файл.
6. Добавлен модуль utils.py, обрабатывает JSON файл и external_api.py, который делает запрос по API.
7. Тестирование
```
pytest
```
Тесты покрывают следующие модули и функции:
- `masks`: функции `get_mask_card_number` и `get_mask_account`.
- `widget`: функции `mask_account_card` и `get_data`.
- `processing`: функции `filter_by_state` и `sort_by_date`.
- `generators`: функции `filter_by_currency`, `transaction_descriptions` и `card_number_generator`.
- `decorators`: функции `log` и `write_log`.
- `utils`: функцию `open_json_file`.
- `external_api`: функцию `converting_transaction`.

Покрытие тестами составляет более 80% кода проекта.
