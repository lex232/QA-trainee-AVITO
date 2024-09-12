"""Тесты API для публикации нового объявления"""
from jsonschema import validate

from api.api import RequestUrl, BodyRequest
from schemes.schemes import (
    valid_announcement_single_exist
)


class TestPostSingleAnnouncement:

    def test_status_code_post_valid_announcement(self):
        """Публикация объявления с корректными параметрами и проверка статус кода"""

        request_body = BodyRequest()
        response = RequestUrl().post_announcement(body=request_body.get_dict())
        assert response.status_code == 201

    def test_data_valid_post_announcement(self):
        """Публикация обявления с корректными параметрами и проверка объявления"""

        request_body = BodyRequest()
        response = RequestUrl().post_announcement(body=request_body.get_dict())

        # Смотрим, какой ID присвоился новому объявлению
        new_id = response.json().get('status').replace('Сохранили объявление - ', '')
        response_after_create = RequestUrl().get_announcement(id_announcement=f'{new_id}')

        # Проверяем что создалось по возвращенному ID
        validate(instance=response_after_create.json()[0], schema=valid_announcement_single_exist)
        assert response_after_create.json()[0].get('name') == request_body.name
        assert response_after_create.json()[0].get('price') == request_body.price
        assert response_after_create.json()[0].get('sellerId') == request_body.seller_id
        assert response_after_create.json()[0].get('statistics').get('contacts') == request_body.contacts
        assert response_after_create.json()[0].get('statistics').get('likes') == request_body.like
        assert response_after_create.json()[0].get('statistics').get('viewCount') == request_body.view_count

    def test_status_code_empty_name_announcement(self, name_empty):
        """Публикация объявления с пустым именем и проверка статус кода"""

        request_body = BodyRequest(name=name_empty)
        response = RequestUrl().post_announcement(body=request_body.get_dict())
        assert response.status_code == 400


    def test_status_code_digit_name_announcement(self, name_digit):
        """Публикация объявления с именем формата int и проверка статус кода"""

        request_body = BodyRequest(name=name_digit)
        response = RequestUrl().post_announcement(body=request_body.get_dict())
        assert response.status_code == 400

    def test_status_code_negative_price_announcement(self, price_negative):
        """Публикация объявления с отрицательной ценой"""

        request_body = BodyRequest(price=price_negative)
        response = RequestUrl().post_announcement(body=request_body.get_dict())
        assert response.status_code == 400

    def test_status_code_word_price_announcement(self, price_word):
        """Публикация объявления с ценой формата String"""

        request_body = BodyRequest(price=price_word)
        response = RequestUrl().post_announcement(body=request_body.get_dict())
        assert response.status_code == 400

    def test_status_code_seller_negative_announcement(self, seller_negative):
        """Публикация объявления с id селлера отрицательным"""

        request_body = BodyRequest(seller_id=seller_negative)
        response = RequestUrl().post_announcement(body=request_body.get_dict())
        assert response.status_code == 400

    def test_status_code_seller_string_announcement(self, seller_string):
        """Публикация объявления с id селлера в формате String"""

        request_body = BodyRequest(seller_id=seller_string)
        response = RequestUrl().post_announcement(body=request_body.get_dict())
        assert response.status_code == 400

    def test_status_code_contacts_negative_announcement(self, contacts_negative):
        """Публикация объявления с контактами отрицательными"""

        request_body = BodyRequest(contacts=contacts_negative)
        response = RequestUrl().post_announcement(body=request_body.get_dict())
        assert response.status_code == 400

    def test_status_code_contacts_string_announcement(self, contacts_string):
        """Публикация объявления с контактами в формате String"""

        request_body = BodyRequest(contacts=contacts_string)
        response = RequestUrl().post_announcement(body=request_body.get_dict())
        assert response.status_code == 400

    def test_status_code_like_negative_announcement(self, like_negative):
        """Публикация объявления с like отрицательным"""

        request_body = BodyRequest(like=like_negative)
        response = RequestUrl().post_announcement(body=request_body.get_dict())
        assert response.status_code == 400

    def test_status_code_like_string_announcement(self, like_string):
        """Публикация объявления с like в формате String"""

        request_body = BodyRequest(like=like_string)
        response = RequestUrl().post_announcement(body=request_body.get_dict())
        assert response.status_code == 400

    def test_status_code_view_negative_announcement(self, view_negative):
        """Публикация объявления с view count отрицательным"""

        request_body = BodyRequest(view_count=view_negative)
        response = RequestUrl().post_announcement(body=request_body.get_dict())
        assert response.status_code == 400

    def test_status_code_view_string_announcement(self, view_string):
        """Публикация объявления с view count в формате String"""

        request_body = BodyRequest(view_count=view_string)
        response = RequestUrl().post_announcement(body=request_body.get_dict())
        assert response.status_code == 400

    def test_status_code_null_announcement(self, view_string):
        """Публикация объявления с одним значением"""

        response = RequestUrl().post_announcement(body={"name": "BMW X6"})
        assert response.status_code == 400

    def test_status_code_obj_null_announcement(self, view_string):
        """Публикация объявления, не передаем объект"""

        response = RequestUrl().post_announcement(body=None)
        assert response.status_code == 400




