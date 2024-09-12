"""Тесты API для получения всех объявлений по ID продавца"""
from jsonschema import validate

from api.api import RequestUrl
from schemes.schemes import (
    valid_announcement_single_exist,
    valid_announcement_single_non_exist
)


class TestGetAllAnnouncementsForSeller:

    def test_get_announcements_exist_seller_id(self, exist_seller_id):
        """Получение объявления по существующему идентификатору продавца"""

        response = RequestUrl().get_all_announcements_seller(seller_id=f'{exist_seller_id}')
        assert response.status_code == 200
        validate(instance=response.json()[0], schema=valid_announcement_single_exist)
        assert response.json()[0].get('sellerId') == int(f'{exist_seller_id}')

    def test_get_announcements_non_exist_seller_id(self, non_exist_seller_id_digit):
        """Получение объявления по несуществующему идентификатору продавца"""

        response = RequestUrl().get_all_announcements_seller(seller_id=f'{non_exist_seller_id_digit}')
        assert response.status_code == 200
        assert response.json() == []

    def test_get_announcements_seller_id_word(self, seller_id_word):
        """Получение объявления по идентификатору продавца в виде слова"""

        response = RequestUrl().get_all_announcements_seller(seller_id=f'{seller_id_word}')
        assert response.status_code == 400
