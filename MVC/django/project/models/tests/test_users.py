from django.test import TestCase
from models.orator import User


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User()
        self.user.name = 'Example User'
        self.user.email = 'user@example.com'

    def test_should_be_valid(self):
        assert self.user
