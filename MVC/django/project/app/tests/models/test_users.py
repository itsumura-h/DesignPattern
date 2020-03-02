import subprocess
from django.test import TestCase
from models.models import User as dUser
from models.orator import User as oUser


class UserTestCase(TestCase):
    def setUp(self):
        subprocess.run(['python', 'manage.py', 'migrate'])
        self.user = oUser.insert({
            'name': 'Example User',
            'email': 'user@example.com'
        })

    def test_should_be_valid(self):
        assert self.user