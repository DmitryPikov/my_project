from typing import Any, Generator


def filter_by_currency(transactions: list, currency: str) -> Generator[Any, Any, None]:
    """Функция фильтрует транзакции по заданной валюте и возвращает итератор"""
    for transaction in transactions:
        if transaction.get("operationAmount").get("currency").get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Generator[Any, Any, None]:
    """Функция возвращает описание каждой операции"""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, stop: int) -> Generator[Any, Any, None]:
    """Функция выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        yield " ".join([card_number[i:i + 4] for i in range(0, 16, 4)])
