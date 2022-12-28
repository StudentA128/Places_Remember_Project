from django.test import TestCase

from placesapp.models import Places


class WorkingWithModelTestCase(TestCase):
    def setUp(self):
        Places.objects.create(
            place_title="Test title 1",
            place_description="Test text for place description 1",
            place_latitude="51.1",
            place_longitude="91.9",
            user_id="user1",
        )
        Places.objects.create(
            place_title="Test title 2",
            place_description="Test text for place description 2",
            place_latitude="52.1",
            place_longitude="92.9",
            user_id="user2",
        )
        Places.objects.create(
            place_title="Test title 3",
            place_description="Test text for place description 3",
            place_latitude="53.1",
            place_longitude="93.9",
            user_id="user1",
        )
        Places.objects.create(
            place_title="Test title 4",
            place_description="Test text for place description 4",
            place_latitude="54.1",
            place_longitude="94.9",
            user_id="user2",
        )

    def test_get_data_from_db(self):
        data_list = Places.objects.filter(user_id="user2")

        result_place_title_1 = data_list[0].place_title
        result_place_description_1 = data_list[0].place_description
        result_place_latitude_1 = data_list[0].place_latitude
        result_place_longitude_1 = data_list[0].place_longitude
        result_user_id_1 = data_list[0].user_id

        result_place_title_2 = data_list[1].place_title
        result_place_description_2 = data_list[1].place_description
        result_place_latitude_2 = data_list[1].place_latitude
        result_place_longitude_2 = data_list[1].place_longitude
        result_user_id_2 = data_list[1].user_id

        self.assertEqual("Test title 2", result_place_title_1)
        self.assertEqual(
            "Test text for place description 2", result_place_description_1
        )
        self.assertEqual(52.1, result_place_latitude_1)
        self.assertEqual(92.9, result_place_longitude_1)
        self.assertEqual("user2", result_user_id_1)

        self.assertEqual("Test title 4", result_place_title_2)
        self.assertEqual(
            "Test text for place description 4", result_place_description_2
        )
        self.assertEqual(54.1, result_place_latitude_2)
        self.assertEqual(94.9, result_place_longitude_2)
        self.assertEqual("user2", result_user_id_2)
