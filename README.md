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
3. Тестирование
```
pytest
```
Тесты покрывают следующие модули и функции:
- `masks`: функции `get_mask_card_number` и `get_mask_account`.
- `widget`: функции `mask_account_card` и `get_data`.
- `processing`: функции `filter_by_state` и `sort_by_date`.

Покрытие тестами составляет более 80% кода проекта.
