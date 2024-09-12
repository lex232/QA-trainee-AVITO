"""Тесты API для получения объявления по его идентификатору"""
from jsonschema import validate

from api.api import RequestUrl
from schemes.schemes import (
    valid_announcement_single_exist,
    valid_announcement_single_non_exist
)


class TestGetSingleAnnouncement:

    def test_get_announcement_exist_id(self, exist_id_announcement):
        """Получение объявления по существующему идентификатору"""

        response = RequestUrl().get_announcement(id_announcement=f'{exist_id_announcement}')
        assert response.status_code == 200
        validate(instance=response.json()[0], schema=valid_announcement_single_exist)
        assert response.json()[0].get('id') == f'{exist_id_announcement}'

    def test_get_announcement_non_exist_id(self, non_exist_id_announcement):
        """Получение объявления по несуществующему идентификатору"""

        response = RequestUrl().get_announcement(id_announcement=f'{non_exist_id_announcement}')
        assert response.status_code == 404
        validate(instance=response.json(), schema=valid_announcement_single_non_exist)
        assert response.json().get('result').get('message') == f'item {non_exist_id_announcement} not found'
