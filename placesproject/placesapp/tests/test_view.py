from django.test import TestCase

from django.urls import reverse


class ViewTest(TestCase):
    def test_view_url_exists_at_desired_location_welcome_page(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_exists_at_desired_location_home_page(self):
        resp = self.client.get("/home")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse("home_page"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("home_page"))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, "placesapp/welcome.html")
