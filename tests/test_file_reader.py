from unittest.mock import Mock, patch

from src.file_reader import csv_reader, excel_reader


@patch("pandas.read_csv")
def test_csv_reader(mock_read_csv: Mock) -> None:
    mock_df = Mock()
    mock_df.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    mock_read_csv.return_value = mock_df
    result = csv_reader("file_path.csv")
    mock_read_csv.assert_called_once_with("file_path.csv", delimiter=";")
    mock_df.to_dict.assert_called_once_with("records")
    expected_result = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    assert result == expected_result


@patch("pandas.read_excel")
def test_excel_reader(mock_read_excel: Mock) -> None:
    mock_df = Mock()
    mock_df.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    mock_read_excel.return_value = mock_df
    result = excel_reader("file_path.xlsx")
    mock_read_excel.assert_called_once_with("file_path.xlsx")
    mock_df.to_dict.assert_called_once_with("records")
    expected_result = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    assert result == expected_result
