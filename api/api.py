"""Модуль запроса"""
import requests


class RequestUrl:
    """Класс запроса для библиотеки requests."""

    def __init__(self):
        self.base_url = 'https://qa-internship.avito.com/'

    API_URL_V = 'api/1/'

    def get_announcement(self, id):
        """URL для получения одного обявления"""

        return requests.get(f"{self.base_url}{self.API_URL_V}item/{id}")

    def get_all_announcement(self, seller_id):
        """URL для получения всех обявлений"""

        return requests.get(f"{self.base_url}{self.API_URL_V}{id}/item")