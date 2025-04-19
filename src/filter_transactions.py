import re
from collections import Counter


def filter_transactions_by_description(transactions: list, search_string: str) -> list:
    """Функция фильтрует список операций, оставляя только те, в описании которых встречается search_string"""
    if not search_string:
        return transactions
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    filtered_transactions = []
    for transaction in transactions:
        description = transaction.get("description", "")
        if pattern.search(description):
            filtered_transactions.append(transaction)
    return filtered_transactions


def count_transactions_by_category(transactions: list, list_categories: list) -> dict:
    """Функция считает количество операций в каждой категории"""
    filtered_categories = []
    for transaction in transactions:
        description = transaction.get("description", "")
        if description in list_categories:
            filtered_categories.append(description)
    counted = Counter(filtered_categories)
    return dict(counted)
