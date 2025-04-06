import os

import requests
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("API_KEY")


def converting_transaction(transaction: dict) -> float:
    """Функция, которая получает транзакцию и возвращает сумму транзакции в рублях"""
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {
        "amount": transaction.get("operationAmount", None).get("amount", None),
        "from": transaction.get("operationAmount", None).get("currency", None).get("code", None),
        "to": "RUB",
    }
    headers = {"apikey": f"{apikey}"}
    response = requests.get(url, headers=headers, params=payload)
    if transaction.get("operationAmount", None).get("currency", None).get("code", None) == "RUB":
        return float(transaction.get("operationAmount", None).get("amount", None))
    elif transaction.get("operationAmount", None).get("currency", None).get("code", None) == "USD" or "EUR":
        return round(float(response.json().get("result")), 2)
    else:
        raise
