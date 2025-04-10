import pandas as pd


def csv_reader(file_path: str) -> list:
    """Функция для считывания финансовых операций из CSV файла, которая выдает список словарей с транзакциями"""
    df = pd.read_csv(file_path, delimiter=";")
    transactions = df.to_dict("records")
    return transactions


def excel_reader(file_path: str) -> list:
    """Функция для считывания финансовых операций из Excel файла, которая выдает список словарей с транзакциями"""
    df = pd.read_excel(file_path)
    transactions = df.to_dict("records")
    return transactions
