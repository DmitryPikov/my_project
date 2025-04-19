import pandas as pd

from src.file_reader import csv_reader, excel_reader
from src.filter_transactions import filter_transactions_by_description
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import open_json_file
from src.widget import get_date, mask_account_card


def main() -> None:
    print(
        "Программа: Привет. Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )

    while True:
        user_input_menu = input("Пользователь: ")
        try:
            if int(user_input_menu) == 1:
                print("Программа. Для обработки выбран JSON-файл.\n")
                transactions = open_json_file("data/operations.json")
                break
            elif int(user_input_menu) == 2:
                print("Программа. Для обработки выбран CSV-файл.\n")
                csv_transactions = csv_reader("data/transactions.csv")
                transactions = []
                for transaction in csv_transactions:
                    transformed = {
                        "id": transaction.get("id", ""),
                        "state": transaction.get("state", ""),
                        "date": transaction.get("date", ""),
                        "operationAmount": {
                            "amount": transaction.get("amount", ""),
                            "currency": {
                                "name": transaction.get("currency_name", ""),
                                "code": transaction.get("currency_code", ""),
                            },
                        },
                        "description": transaction.get("description", ""),
                    }
                    if "from" in transaction and not pd.isna(transaction["from"]):
                        transformed["from"] = transaction["from"]
                    if "to" in transaction:
                        transformed["to"] = transaction["to"]
                    transactions.append(transformed)
                break
            elif int(user_input_menu) == 3:
                print("Программа. Для обработки выбран XLSX-файл.\n")
                xlsx_transactions = excel_reader("data/transactions_excel.xlsx")
                transactions = []
                for transaction in xlsx_transactions:
                    transformed = {
                        "id": transaction.get("id", ""),
                        "state": transaction.get("state", ""),
                        "date": transaction.get("date", ""),
                        "operationAmount": {
                            "amount": transaction.get("amount", ""),
                            "currency": {
                                "name": transaction.get("currency_name", ""),
                                "code": transaction.get("currency_code", ""),
                            },
                        },
                        "description": transaction.get("description", ""),
                    }
                    if "from" in transaction and not pd.isna(transaction["from"]):
                        transformed["from"] = transaction["from"]
                    if "to" in transaction:
                        transformed["to"] = transaction["to"]
                    transactions.append(transformed)
                break
            else:
                print("Такого пункта меню нет. Выберите необходимый пункт меню 1, 2 или 3.\n")
        except ValueError:
            print("Выберите необходимый пункт меню 1, 2 или 3.\n")

    while True:
        while True:
            print(
                "Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
            user_input_filter = input("Пользователь: ").strip().upper()
            if user_input_filter in ["EXECUTED", "CANCELED", "PENDING"]:
                state = user_input_filter
                transactions = filter_by_state(transactions, state)
                break
            else:
                print(f'Программа: Статус операции "{user_input_filter}" недоступен.\n')
        print(f'Программа: Операции отфильтрованы по статусу "{user_input_filter}"')
        break

    while True:
        print("\nПрограмма: Отсортировать операции по дате? Да/Нет")
        user_input_sort_by_date = input("Пользователь: ").strip().lower()
        if user_input_sort_by_date == "да":
            while True:
                print("\nПрограмма: Отсортировать по возрастанию или по убыванию?")
                user_input_sorting = input("Пользователь: ").strip().lower()
                if user_input_sorting in ["по возрастанию", "по убыванию"]:
                    transactions = sort_by_date(
                        transactions, reverse=True if user_input_sorting == "по убыванию" else False
                    )
                    break
                else:
                    print("\nВозможные варианты выбора: По возрастанию/По убыванию")
            break
        elif user_input_sort_by_date == "нет":
            break
        else:
            print("\nВозможные варианты выбора: Да/Нет")

    while True:
        print("\nПрограмма: Выводить только рублевые транзакции? Да/Нет")
        user_input_currency = input("Пользователь: ").strip().lower()
        if user_input_currency == "да":
            transactions = list(filter_by_currency(transactions, "RUB"))
            break
        elif user_input_currency == "нет":
            break
        else:
            print("\nВозможные варианты выбора: да/нет")

    while True:
        print("\nПрограмма: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_input_filter_by_description = input("Пользователь: ").strip().lower()
        if user_input_filter_by_description == "да":
            user_input_filter_world = input("\nВведите строку для поиска: ").strip()
            transactions = filter_transactions_by_description(transactions, user_input_filter_world)
            break
        elif user_input_filter_by_description == "нет":
            break
        else:
            print("\nВозможные варианты выбора: да/нет")
    if transactions:
        print(
            "\nПрограмма: Распечатываю итоговый список транзакций..."
            "\nПрограмма:"
            f"\nВсего банковских операций в выборке: {len(transactions)}"
        )
    else:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    for transaction in transactions:
        print(f"\n{get_date(transaction.get("date", ""))} {transaction.get("description", "")}")
        print(
            f"{mask_account_card(transaction.get("from", ""))} -> {mask_account_card(transaction.get("to", ""))}"
            if transaction.get("from")
            else f"{mask_account_card(transaction.get("to", ""))}"
        )
        print(
            f"Сумма: {transaction.get("operationAmount", "").get("amount", "")}"
            " "
            f"{transaction.get("operationAmount", "").get("currency", "").get("name", "")}"
        )


if __name__ == "__main__":
    main()
