from django.test import TestCase

from placesapp.models import Places


class WorkingWithModelTestCase(TestCase):
    def test_add_data_to_db(self):
        Places.objects.create(
            place_title="Test title",
            place_description="Test text for place description",
            place_latitude="56.1",
            place_longitude="92.9",
            user_id="user",
        )

        data_list = Places.objects.get(user_id="user")

        result_place_title = data_list.place_title
        result_place_description = data_list.place_description
        result_place_latitude = data_list.place_latitude
        result_place_longitude = data_list.place_longitude
        result_user_id = data_list.user_id

        self.assertEqual("Test title", result_place_title)
        self.assertEqual("Test text for place description", result_place_description)
        self.assertEqual(56.1, result_place_latitude)
        self.assertEqual(92.9, result_place_longitude)
        self.assertEqual("user", result_user_id)
