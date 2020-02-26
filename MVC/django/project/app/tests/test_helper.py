from django.test import TestCase
from app.templatetags.helper import (
    full_title
)

class ApplicationHelperTestCase(TestCase):
    def test_full_title(self):
        self.assertEqual(full_title(), 'Ruby on Rails Tutorial Sample App')
        self.assertEqual(full_title('Help'), 'Help | Ruby on Rails Tutorial Sample App')
