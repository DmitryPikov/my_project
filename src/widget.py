from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    account_card_list = account_card.split()
    if "Счет" in account_card_list:
        return f"{account_card_list[0]} {get_mask_account(int(account_card_list[-1]))}"
    else:
        return f"{" ".join(account_card_list[:-1])} {get_mask_card_number(int(account_card_list[-1]))}"
