from django.test import Client, TestCase
from rest_framework.test import APIClient
from rest_framework import status


class APIIndexTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.base_url = "/"

    def test_index_endpoint(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

