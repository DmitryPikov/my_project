import json
from unittest.mock import mock_open, patch

from src.utils import open_json_file

transaction = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
]


def test_load_correct_transactions() -> None:
    """Тест загрузки корректного JSON-файла"""
    mock_json_content = json.dumps(transaction)
    with patch("builtins.open", mock_open(read_data=mock_json_content)) as mock_file:
        result = open_json_file("dummy_path.json")
        mock_file.assert_called_once_with("dummy_path.json", "r", encoding="utf-8")
        assert result == transaction


def test_load_empty_file() -> None:
    """Тест пустого файла (должен вернуть [])"""
    with patch("builtins.open", mock_open(read_data="")) as mock_file:
        assert open_json_file("empty.json") == []
        mock_file.assert_called_once_with("empty.json", "r", encoding="utf-8")


def test_load_invalid_json() -> None:
    """Тест некорректного JSON (должен вернуть [])"""
    with patch("builtins.open", mock_open(read_data="{invalid_json: 123}")):
        assert open_json_file("invalid.json") == []


def test_load_non_list_json() -> None:
    """Тест JSON, который не является списком (должен вернуть [])"""
    with patch("builtins.open", mock_open(read_data='{"id": 1, "amount": 100}')):
        assert open_json_file("not_a_list.json") == []


def test_file_not_found() -> None:
    """Тест несуществующего файла (должен вернуть [])"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        assert open_json_file("nonexistent.json") == []


def test_json_decode_error() -> None:
    """Тест ошибки декодирования JSON (должен вернуть [])"""
    with patch("json.load", side_effect=json.JSONDecodeError("Error", "doc", 0)):
        with patch("builtins.open", mock_open(read_data="invalid")):
            assert open_json_file("bad_json.json") == []
