import subprocess
from django.test import TestCase
from models.validation import User
from models.orator import User as DbUser


class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        subprocess.run(['python', 'manage.py', 'flush'])

    def setUp(self):
        self.name = 'Example User'
        self.email = 'user@example.com'
        self.password = 'foobar'

    def test_001_should_be_valid(self):
        user = User(name=self.name, email=self.email, password=self.password)
        self.assertTrue(user.valid())

    def test_002_name_should_be_present(self):
        name = ''
        user = User(name=name, email=self.email, password=self.password)
        self.assertFalse(user.valid())

    def test_003_email_should_be_present(self):
        email = '   '
        user = User(name=self.name, email=email, password=self.password)
        self.assertFalse(user.valid())

    def test_004_name_should_not_be_too_long(self):
        name = 'a' * 51
        user = User(name=name, email=self.email, password=self.password)
        self.assertFalse(user.valid())

    def test_005_email_should_not_be_too_long(self):
        email = 'a' * 244 + '@example.com'
        user = User(name=self.name, email=email, password=self.password)
        self.assertFalse(user.valid())

    def test_006_email_validation_should_accept_valid_addresses(self):
        valid_addresses = [
            'user@example.com',
            'USER@foo.COM',
            'A_US-ER@foo.bar.org',
            'first.last@foo.jp',
            'alice+bob@baz.cn'
        ]

        for valid_address in valid_addresses:
            user = User(name=self.name, email=valid_address, password=self.password)
            self.assertTrue(user.valid())

    def test_007_email_validation_should_not_valid(self):
        valid_addresses = [
            'alice+bob@baz.',
            'foo@bar..com'
        ]

        for valid_address in valid_addresses:
            user = User(name=self.name, email=valid_address, password=self.password)
            self.assertFalse(user.valid())

    def test_008_email_addresses_should_be_unique(self):
        DbUser.insert({
            'name': self.name,
            'email': self.email,
            'password': self.password
        })
        user = User(name=self.name, email=self.email, password=self.password)
        self.assertFalse(user.valid())

    def test_009_password_should_be_present(self):
        password = ' ' * 6
        user = User(name=self.name, email=self.email, password=password)
        self.assertFalse(user.valid())

    def test_010password_should_have_a_minimum_length(self):
        password = ' ' * 5
        user = User(name=self.name, email=self.email, password=password)
        self.assertFalse(user.valid())