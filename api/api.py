"""Модуль запроса"""
import requests


class RequestUrl:
    """Класс запроса для библиотеки requests."""

    def __init__(self):
        self.base_url = 'https://qa-internship.avito.com/'

    API_URL_V = 'api/1/'

    def get_announcement(self, id_announcement):
        """URL для получения одного объявления"""

        return requests.get(f"{self.base_url}{self.API_URL_V}item/{id_announcement}")

    def get_all_announcements_seller(self, seller_id):
        """URL для получения всех объявлений продавца"""

        return requests.get(f"{self.base_url}{self.API_URL_V}{seller_id}/item")

    def post_announcement(self, body):
        """URL для публикации объявления"""

        return requests.post(f"{self.base_url}{self.API_URL_V}/item", json=body)


class BodyRequest:
    """Класс формирования тела запроса для создания объявления с корректными данными."""

    def __init__(
            self,
            name='BMW X6',
            price=232000,
            seller_id=232232,
            contacts=232,
            like=20,
            view_count=15
    ):
        self.name = name
        self.price = price
        self.seller_id = seller_id
        self.contacts = contacts
        self.like = like
        self.view_count = view_count

    def get_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "sellerId": self.seller_id,
            "statistics": {
                "contacts": self.contacts,
                "like": self.like,
                "viewCount": self.view_count
            }
        }
