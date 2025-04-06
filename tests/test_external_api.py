import json
import os
from unittest.mock import patch

from dotenv import load_dotenv
from mypy.types import AnyType

from src.external_api import converting_transaction

load_dotenv()
apikey = os.getenv("API_KEY")


transaction_rub = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}


transaction_usd = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}


@patch("requests.get")
def test_converting_transaction_rub(mock_get):
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {
        "amount": transaction_rub.get("operationAmount").get("amount"),
        "from": transaction_rub.get("operationAmount").get("currency").get("code"),
        "to": "RUB",
    }
    headers = {"apikey": f"{apikey}"}
    mock_get.return_value.json.return_value = 31957.58
    assert converting_transaction(transaction_rub) == 31957.58
    mock_get.assert_called_once_with(url, headers=headers, params=payload)


@patch("requests.get")
def test_converting_transaction_usd(mock_get):
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {
        "amount": transaction_usd.get("operationAmount").get("amount"),
        "from": transaction_usd.get("operationAmount").get("currency").get("code"),
        "to": "RUB",
    }
    headers = {"apikey": f"{apikey}"}
    mock_get.return_value.json.return_value = {"result": "8221.37"}
    assert converting_transaction(transaction_usd) == 8221.37
    mock_get.assert_called_once_with(url, headers=headers, params=payload)
