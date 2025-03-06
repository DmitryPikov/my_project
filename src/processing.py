def filter_by_state(list_dictionaries: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей у которых ключ state соответствует указанному значению"""
    list_by_state = []
    for item in list_dictionaries:
        if item.get("state") == state:
            list_by_state.append(item)
    return list_by_state
