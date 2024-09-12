"""Фикстуры pytest"""
import pytest


@pytest.fixture
def exist_id_announcement():
    """Cуществующий ID обявления"""

    return "58081ae6-0244-4c1c-b9e6-d408cab9bd1d"

@pytest.fixture
def non_exist_id_announcement():
    """Не существующий ID обявления"""

    return "aaaa1111-ssss-dddd-eeee-dddd2222bbbb"

@pytest.fixture
def exist_seller_id():
    """Cуществующий ID обявления"""

    return "232232"

@pytest.fixture
def non_exist_seller_id_digit():
    """Не существующий ID обявления"""

    return "10101001010"

@pytest.fixture
def seller_id_word():
    """Не корректный ID обявления (символы, вместо цифр)"""

    return "qwerty"
