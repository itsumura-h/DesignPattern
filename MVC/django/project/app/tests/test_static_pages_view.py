from django.test import TestCase


class StaticPageViewTestCase(TestCase):
    def test_should_get_home_url(self):
        response = self.client.get('/static_pages/home/')
        self.assertEqual(response.status_code, 200)

    def test_should_get_help(self):
        response = self.client.get('/static_pages/help/')
        self.assertEqual(response.status_code, 200)

    def test_should_get_about(self):
        response = self.client.get('/static_pages/about/')
        self.assertEqual(response.status_code, 200)