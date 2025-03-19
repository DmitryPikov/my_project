import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(list_dictionary_with_state: list) -> None:
    assert filter_by_state(list_dictionary_with_state, state="EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_canceled(list_dictionary_with_state: list) -> None:
    assert filter_by_state(list_dictionary_with_state, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_incorrect_value(list_dictionary_without_state: list) -> None:
    with pytest.raises(Exception) as exc_info:
        filter_by_state(list_dictionary_without_state)

    assert str(exc_info.value) == "Не корректные данные"


def test_sort_by_date(list_dictionary: list) -> None:
    assert sort_by_date(list_dictionary, reverse=True) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_reverse(list_dictionary: list) -> None:
    assert sort_by_date(list_dictionary, reverse=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.mark.parametrize(
    "list_dictionary, expected",
    [
        ([], "Не корректные данные"),
        (None, "Не корректные данные"),
    ],
)
def test_sort_date_incorrect_value(list_dictionary: list, expected: str):
    with pytest.raises(Exception) as exc_info:
        sort_by_date(list_dictionary)

    assert str(exc_info.value) == expected
