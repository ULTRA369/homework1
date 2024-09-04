from typing import Any


def filter_by_state(input_list: list[Any], state="EXECUTED") -> Any:
    """Функция фильтрации операций по ключу state"""

    filtered_list = []
    if len(input_list) > 0:
        for element in input_list:
            if element.get("state") == state:
                filtered_list.append(element)

        return filtered_list
    else:
        return "Список пуст"


def sort_by_date(input_list: list[Any], descending=True) -> Any:
    """Функция сортировки операций по дате"""
    if len(input_list) > 0:
        sorted_list = sorted(
            input_list, key=lambda x: x.get("date"), reverse=descending
        )
        return sorted_list
    else:
        return "Список пуст"
