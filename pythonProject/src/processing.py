def filter_by_state(dict_list, state='EXECUTED'):
    """Функция оставляет только выполненные операции по ключу EXECUTED"""
    result = []
    for i in dict_list:
        if i.get('state') == state:
            result.append(i)
    return result


data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

filtered_data = filter_by_state(data)
print(filtered_data)


def sort_by_date(operations_data: list[dict]) -> list[dict]:
    """Сортирует список по дате"""
    sorted_list = sorted(operations_data, key=lambda x: x['date'], reverse=True)
    return sorted_list


data_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

print(sort_by_date(data_list))
