import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: list) -> None:
    usd_transactions = filter_by_currency(transactions, currency="USD")
    rub_transactions = filter_by_currency(transactions, currency="RUB")
    assert next(usd_transactions) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(usd_transactions) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(rub_transactions) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(rub_transactions) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        ([], "EUR", []),
    ],
)
def test_filter_by_currency_no_matching_currency(transactions: list, currency: str, expected: str) -> None:
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        ([], "USD", []),
    ],
)
def test_filter_by_currency_empty_list(transactions: list, currency: str, expected: str) -> None:
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


def test_transaction_descriptions(transactions: list) -> None:
    description = list(transaction_descriptions(transactions))
    assert description == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.mark.parametrize(
    "transactions, expected",
    [
        ([], []),
    ],
)
def test_transaction_descriptions_empty_list(transactions: list, expected: list) -> None:
    result = list(transaction_descriptions(transactions))
    assert result == expected


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            4000123456789010,
            4000123456789014,
            [
                "4000 1234 5678 9010",
                "4000 1234 5678 9011",
                "4000 1234 5678 9012",
                "4000 1234 5678 9013",
                "4000 1234 5678 9014",
            ],
        ),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: list) -> None:
    assert list(card_number_generator(start, stop)) == expected
