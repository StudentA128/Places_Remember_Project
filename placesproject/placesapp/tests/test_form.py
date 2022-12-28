from django.test import TestCase

from placesapp.forms import PlacesForm


class PlacesFormTestCase(TestCase):
    def test_form_fields(self):
        form = PlacesForm()

        expected_form_fields_list = [
            "place_title",
            "place_description",
            "place_latitude",
            "place_longitude",
            "user_id",
        ]

        self.assertEqual(list(form.fields.keys()), expected_form_fields_list)

    def test_form_fields_value(self):
        form = PlacesForm()

        place_title_value = "Test place title"
        place_description_value = "Test place description"
        place_latitude_value = "52.3"
        place_longitude_value = "97.4"
        user_id_value = "user"

        form.fields["place_title"] = place_title_value
        form.fields["place_description"] = place_description_value
        form.fields["place_latitude"] = place_latitude_value
        form.fields["place_longitude"] = place_longitude_value
        form.fields["user_id"] = user_id_value

        self.assertEqual(form.fields["place_title"], "Test place title")
        self.assertEqual(form.fields["place_description"], "Test place description")
        self.assertEqual(form.fields["place_latitude"], "52.3")
        self.assertEqual(form.fields["place_longitude"], "97.4")
        self.assertEqual(form.fields["user_id"], "user")

    def test_incorrect_form(self):
        form = PlacesForm()

        place_title_value = "Test place title"
        user_id_value = "user"

        form.fields["place_title"] = place_title_value
        form.fields["user_id"] = user_id_value

        self.assertFalse(form.is_valid())
