import json


def open_json_file(file_path: str) -> list:
    """Функция, которая принимает на вход JSON файл и возвращает список словарей"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        else:
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
