from django.test import Client, TestCase
from rest_framework.test import APIClient
from rest_framework import status

from democratic_api.models import Nationality
from democratic_api.tests.utils import DataBaseSetupMixin


class APITestCase(TestCase, DataBaseSetupMixin):
    def setUp(self):
        self.client = APIClient()
        self.base_url = "/api/"
        self.set_up_database()

    def test_index_endpoint(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_successful_border_crossing_creation(self):
        nationality = self.db_default_nationality
        valid_data = {
            "forbidden_stuff": [],
            "border_crossing": [{"allowed": True}],
            "first_name": "Tomas",
            "last_name": "York",
            "date_of_birth": "1988-04-13",
            "living_address": "Ukraine, Lviv, Horbachevskogo, 21",
            "phone_number": "558005353535",
            "height": 1.8,
            "color_of_eyes": "blue",
            "nationality": nationality,
        }

        response = self.client.post(
            self.base_url + "person_border_crossing/", data=valid_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
