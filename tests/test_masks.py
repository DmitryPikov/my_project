import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number(2015968378687051) == "2015 96** **** 7051"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (715830073472675806, "Не корректный номер карты"),
        ("", "Не корректный номер карты"),
        (None, "Не корректный номер карты"),
    ],
)
def test_get_mask_card_number_with_incorrect_value(card_number: int, expected: str) -> None:
    with pytest.raises(Exception) as exc_info:
        get_mask_card_number(card_number)

    assert str(exc_info.value) == expected


def test_get_mask_account() -> None:
    assert get_mask_account(64686473678894779589) == "**9589"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        (353830334744478955, "Не корректный номер счета"),
        ("", "Не корректный номер счета"),
        (None, "Не корректный номер счета"),
    ],
)
def test_get_mask_account_with_incorrect_value(account_number: int, expected: str) -> None:
    with pytest.raises(Exception) as exc_info:
        get_mask_account(account_number)

    assert str(exc_info.value) == expected
