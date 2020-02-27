from django.test import TestCase
from rest_framework.test import APITestCase
from django_webtest import WebTest


class UserViewTestCase(WebTest):
    def setUp(self):
        self.base_title = 'Ruby on Rails Tutorial Sample App'

    def test_should_get_create(self):
        response = self.app.get('/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.html.title.text, f'Sign up | {self.base_title}')
