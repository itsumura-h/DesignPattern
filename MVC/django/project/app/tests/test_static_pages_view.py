from django.test import TestCase
from django_webtest import WebTest


class StaticPageViewWebTestCase(WebTest):
    def setUp(self):
        self.base_title = 'Ruby on Rails Tutorial Sample App'

    def test_should_get_home_url(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.html.title.text, f'Home | {self.base_title}')

    def test_should_get_help(self):
        response = self.app.get('/help/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.html.title.text, f'Help | {self.base_title}')

    def test_should_get_about(self):
        response = self.app.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.html.title.text, f'About | {self.base_title}')

    def test_should_get_contact(self):
        response = self.app.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.html.title.text, f'Contact | {self.base_title}')
