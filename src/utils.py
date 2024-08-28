import json
import logging
from json import JSONDecodeError

logger = logging.getLogger('utils')  # создаем логер
logger.setLevel(logging.DEBUG)  # уровень вывода сообщения не меньше DEBUG
logger.filemode = 'w'  # Перезапись файла при каждом запуске
# создаем хендлер и указываем в какой папке будет лог и имя лога:
file_handler = logging.FileHandler('../logs/utils.log')
# создаем и настраиваем  форматтер логера:
file_formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)  # подключаем к логгеру форматтер
logger.addHandler(file_handler)  # подключаем к логгеру хендлер


def financial_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        logger.info("Открытие файла %s", path)
        with open(path, encoding="utf-8") as financial_file:
            try:
                logger.info("Получение информации о транзакциях %s", path)
                transactions = json.load(financial_file)
            except JSONDecodeError:
                logger.error("Невозможно декодировать файл %s", path)
                return []
        if not isinstance(transactions, list):
            return []
        return transactions
    except FileNotFoundError:
        logger.error("Путь к файлу %s не найден", path)
        return []
