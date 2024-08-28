import logging


logger = logging.getLogger('utils')    # создаем логер
logger.setLevel(logging.DEBUG)    # уровень вывода сообщения не меньше DEBUG
# создаем хендлер и указываем в какой папке будет лог и имя лога:
file_handler = logging.FileHandler('../logs/masks.log')
# создаем и настраиваем  форматтер логера:
file_formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)    # подключаем к логгеру форматтер
logger.addHandler(file_handler)    # подключаем к логгеру хендлер

def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    logger.info("Маскируем банковскую карту клиента")

    if card_number.isdigit() and len(card_number) == 16:
        logger.info("Маска карты сформирована успешно")
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        logger.error("Неверный формат входных данных")
        return "Номер карты должен состоять из 16 цифр"


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    logger.info("Маскируем банковский счет клиента")
    if account.isdigit() and len(account) == 20:
        logger.info("Маска счета сформирована успешно")
        return f"{'*' * 2}{account[16:]}"
    else:
        logger.error("Неверный формат входных данных")
        return "Номер счета должен состоять из 20 цифр"
