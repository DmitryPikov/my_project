import json
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/utils.log', 'w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def open_json_file(file_path: str) -> list:
    """Функция, которая принимает на вход JSON файл и возвращает список словарей"""
    try:
        logger.debug("Открываем файл JSON")
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            logger.info("Возвращаем список словарей")
            return data
        else:
            return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Произошла ошибка {e}")
        return []
