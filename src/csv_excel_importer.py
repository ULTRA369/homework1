import csv

import pandas as pd


def csv_import(path_file):
    """Функция принимает аргументом путь к файлу .csv и возвращает список словарей с транзакциями"""
    transactions = []
    try:
        with open(path_file, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # закоментируй строку чтобы выdодилась первая строка тоже
            for row in reader:
                transactions.append(row)
    except Exception as e:
        print(f"Ошибка при считывании файла: {e}")
    return transactions


def excel_import(path_file):
    """Функция принимает аргументом путь к файлу Excel и возвращает список словарей с транзакциями, в котором ключами
     служат названия столбцов"""
    try:
        excel_data = pd.read_excel(path_file)
        transactions = excel_data.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при считывании файла: {e}")
        return []
