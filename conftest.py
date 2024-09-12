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

@pytest.fixture
def name_empty():
    """Имя объявления пустое"""

    return ""

@pytest.fixture
def name_digit():
    """Имя объявления int"""

    return 232323

@pytest.fixture
def price_negative():
    """Цена объявления отрицательная"""

    return -1222

@pytest.fixture
def price_word():
    """Цена объявления отрицательная"""

    return 'hello world'

@pytest.fixture
def seller_negative():
    """ID селлера отрицательный"""

    return -232232

@pytest.fixture
def seller_string():
    """ID селлера в формате String"""

    return "seller word"

@pytest.fixture
def contacts_negative():
    """контакты отрицательные"""

    return -23

@pytest.fixture
def contacts_string():
    """контакты в формате String"""

    return "contacts word"

@pytest.fixture
def like_negative():
    """like отрицательный"""

    return -33

@pytest.fixture
def like_string():
    """like в формате String"""

    return "like word"

@pytest.fixture
def view_negative():
    """view count отрицательный"""

    return -17

@pytest.fixture
def view_string():
    """view count в формате String"""

    return "view word"