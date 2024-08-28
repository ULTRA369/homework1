# `Программа для банковских операций`

Программа создана для фильтрации и сортировки замаскированных банковских счетов по дате и оплате.

___________________________________________________________________________________________

## Структура проекта

### Модуль masks

- Функция `get_mask_card_number` принимает номер карты и возвращает ее маску
- Функция `get_mask_account` приниает номер и счета и возвращает его маску

### Модуль widget

- Функция `mask_account_card` умеет обрабатывать информацию как о картах, так и о счетах
- Функция `get_data` принимает и преобразует формат даты

### Модуль processing

- Функция `filter_by_state` возвращает новый список словарей, содержащий только те словари, у которых ключ state
  соответствует указанному значению
- Функция `sort_by_date` принимает список словарей и необязательный параметр, задающий порядок сортировки

### Модуль generators

- Функция `filter_by_cerrency` принимает на вход список словарей, представляющих транзакции и возвращать итератор,
  который поочередно выдает транзакции, где валюта операции соответствует заданной
- Генератор `transaction_descriptions` принимает список словарей с транзакциями и возвращает описание каждой операции по
  очереди.
- Генератор `card_number_generator` может сгенерировать номера карт в заданном диапазоне

### Модуль utils

- Функция `financial_transactions` принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список.

### Модуль external_api

- Функция `get_exchange_amount`принимает на вход транзакцию и возвращает сумму транзакции в рублях. Если транзакция в Евро или долларах то обращается к стороннему сервису через API и конвертирует по текущему курсу


_____

## Тестирование

- Для запуска тестов введите команду `pytest`

_____

## Обновления

Информацию об обновлениях проекта можно найти в [документации](update.md)

-----

## Автор проекта

`Svetlana Linberg` - [ya.vgb@list.ru]
