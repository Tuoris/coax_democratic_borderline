from copy import deepcopy

from django.test import TestCase

from democratic_api.serializers import PersonBorderCrossingSerializer
from democratic_api.tests.utils import DataBaseSetupMixin


class PersonBorderCrossingSerializerTestCase(TestCase, DataBaseSetupMixin):
    def setUp(self):
        self.set_up_database()
        nationality = self.db_default_nationality
        self.valid_data = {
            "forbidden_stuff": [{"description": "Guns"}],
            "border_crossing": [{"allowed": False}],
            "first_name": "Mike",
            "last_name": "Bay",
            "date_of_birth": "1998-04-13",
            "living_address": "Ukraine, Lviv, Horbachevskogo, 21",
            "phone_number": "558005353535",
            "height": 1.79,
            "color_of_eyes": "brown",
            "nationality": nationality,
        }

    def test_success_creation_with_valid_data(self):
        serializer = PersonBorderCrossingSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertFalse(serializer.errors)

    def test_success_update_with_valid_data(self):
        valid_data = deepcopy(self.valid_data)
        new_height = 1.80
        corrected_color_of_eyes = "brownish"
        valid_data.update(
            {
                "forbidden_stuff": [],
                "border_crossing": [],
                "color_of_eyes": corrected_color_of_eyes,
                "height": new_height,
            }
        )
        serializer = PersonBorderCrossingSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertFalse(serializer.errors)

        self.assertEqual(serializer.validated_data["height"], new_height)
        self.assertEqual(
            serializer.validated_data["color_of_eyes"], corrected_color_of_eyes
        )

    def test_success_adding_new_borderline_cross(self):
        valid_data = deepcopy(self.valid_data)
        valid_data.update(
            {"forbidden_stuff": [], "border_crossing": [{"allowed": True}]}
        )
        serializer = PersonBorderCrossingSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertFalse(serializer.errors)
