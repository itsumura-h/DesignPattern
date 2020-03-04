import subprocess
from django.test import TestCase
from models.validation import User


class UserTestCase(TestCase):
    def setUp(self):
        self.name = 'Example User'
        self.email = 'user@example.com'

    def test_should_be_valid(self):
        user = User(name=self.name, email=self.email)
        self.assertTrue(user.valid())

    def test_name_should_be_present(self):
        name = ''
        user = User(name=name, email=self.email)
        self.assertFalse(user.valid())

    def test_email_should_be_present(self):
        email = '   '
        user = User(name=self.name, email=email)
        self.assertFalse(user.valid())

    def test_name_should_not_be_too_long(self):
        name = 'a' * 51
        user = User(name=name, email=self.email)
        self.assertFalse(user.valid())

    def test_email_should_not_be_too_long(self):
        email = 'a' * 244 + '@example.com'
        user = User(name=self.name, email=email)
        self.assertFalse(user.valid())

    def test_email_validation_should_accept_valid_addresses(self):
        valid_addresses = [
            'user@example.com',
            'USER@foo.COM',
            'A_US-ER@foo.bar.org',
            'first.last@foo.jp',
            'alice+bob@baz.cn'
        ]

        for valid_address in valid_addresses:
            user = User(name=self.name, email=valid_address)
            self.assertTrue(user.valid)