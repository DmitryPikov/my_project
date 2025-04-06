import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log', 'w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    card_number_str = str(card_number)
    if len(card_number_str) != 16 or not card_number_str.isdigit() or card_number_str == "" or card_number_str is None:
        logger.error("Не корректный номер карты")
        raise Exception("Не корректный номер карты")
    else:
        logger.info("Успешная маскировка банковской карты")
        return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    account_number_str = str(account_number)
    if (
        len(account_number_str) != 20
        or not account_number_str.isdigit()
        or account_number_str == ""
        or account_number_str is None
    ):
        logger.error("Не корректный номер счета")
        raise Exception("Не корректный номер счета")
    else:
        logger.info("Успешная маскировка банковского счета")
        return f"**{account_number_str[-4:]}"
