import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("700079228960636", "Номер карты должен состоять из 16 цифр"),
        ("a00079228960636", "Номер карты должен состоять из 16 цифр"),
        ("70007922896063612", "Номер карты должен состоять из 16 цифр"),
    ],
)
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize(
    "account, expected_acc",
    [
        ("73654108430135874305", "**4305"),
        ("700079228960636", "Номер счета должен состоять из 20 цифр"),
        ("7365410843013587430a", "Номер счета должен состоять из 20 цифр"),
        ("736541084301358743051", "Номер счета должен состоять из 20 цифр"),
    ],
)
def test_get_mask_account(account, expected_acc):
    assert get_mask_account(account) == expected_acc
