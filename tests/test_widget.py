import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ],
)
def test_mask_account_card(account_card: str, expected: str) -> None:
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("", "Не корректные данные"),
        (None, "Не корректные данные"),
    ],
)
def test_mask_account_card_with_incorrect_value(account_card: str, expected: str) -> None:
    with pytest.raises(Exception) as exc_info:
        mask_account_card(account_card)

    assert str(exc_info.value) == expected


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize(
    "date_time, expected",
    [
        ("", "Не корректные данные"),
        (None, "Не корректные данные"),
    ],
)
def test_get_date_with_incorrect_value(date_time: str, expected: str) -> None:
    with pytest.raises(Exception) as exc_info:
        get_date(date_time)

    assert str(exc_info.value) == expected
