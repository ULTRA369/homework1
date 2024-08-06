def get_mask_card_number(card_number: str) -> str:
    """Функция, которая возвращает маску карты"""
    masked_card = card_number[:4] + " " + card_number[4:6] + "** ****" + " " + card_number[-4:]
    return masked_card


def get_mask_account(account_number: str) -> str:
    """Функция, которая возвращает маску счета"""
    masked_account_number = "**" + account_number[-4:]
    return masked_account_number
