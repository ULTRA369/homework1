import json
from json import JSONDecodeError
import requests

from src.external_api import get_exchange_amount


def financial_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, encoding='utf-8') as financial_file:
            try:
                transactions = json.load(financial_file)
            except JSONDecodeError:
                return []
        if not isinstance(transactions, list):
            return []
        return transactions
    except FileNotFoundError:
        return []


def get_transaction_amount(trans: dict, currency: str = "RUB") -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
    else:
        amount = get_exchange_amount(trans)
    return amount