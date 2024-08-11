import pytest


@pytest.fixture
def by_state():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def account_numbers():
    return [("1234567890", "Счет **7890"), ("9876543210", "Счет **3210"), ("12345", "Счет **2345")]


@pytest.fixture
def card_numbers():
    return [
        ("Visa 1234 5678 9012 3456", "Visa 1234 56** **** 3456"),
        ("Maestro 9876 5432 1098 7654", "Maestro 9876 54** **** 7654"),
        ("123456789012345", "Неверный формат входных данных"),
    ]


@pytest.fixture
def sample_data():
    return [
        {"date": "2023-12-31T15:30:00.000", "state": "EXECUTED"},
        {"date": "2022-08-15T10:45:00.000", "state": "PENDING"},
        {"date": "2024-05-20T18:00:00.000", "state": "EXECUTED"},
    ]
