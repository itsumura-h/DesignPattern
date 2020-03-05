import re
from models.orator import User as DbUser
from cerberus import Validator


class User:
    class Name:
        errors = []
        value = ''

        def __init__(self, value):
            schema = {
                'value': {
                    'type': 'string',
                    'required': True,
                    'empty': False,
                    'max': 50
                }
            }
            if len(value) == 0:
                self.errors.append('name is required')
                self.value = None

            pattern = re.compile(r'^(\w)+')
            if not pattern.match(value):
                self.errors.append('name not allow blank')
                self.value = None

            if len(value) > 50:
                self.errors.append('name should be shorter than 50')
                self.value = None

            if self.value is None:
                return None

            self.value = value

    class Email:
        errors = []
        value = ''

        def __init__(self, value):
            if len(value) == 0:
                self.errors.append('email is required')
                self.value = None

            pattern = re.compile(r'^(\w)+')
            if not pattern.match(value):
                self.errors.append('email not allow blank')
                self.value = None

            if len(value) > 255:
                self.errors.append('email should be shorter than 255')
                self.value = None

            pattern = re.compile(
                r"\A[\w+\-.]+@[a-zA-Z\d\-]+(\.[a-zA-Z\d\-]+)*\.[a-zA-Z]+\Z")
            if not pattern.match(value):
                self.errors.append('invalid form of email')
                self.value = None

            if DbUser.where('email', value).count() > 0:
                self.errors.append('email should be unique')
                self.value = None

            if self.value is None:
                return None

            self.value = value

    class Password:
        errors = []
        value = ''

        def __init__(self, value):
            if len(value) == 0:
                self.errors.append('password is required')
                self.value = None

            pattern = re.compile(r'^(\w)+')
            if not pattern.match(value):
                self.errors.append('password not allow blank')
                self.value = None

            if len(value) < 6:
                self.errors.append('password should be longer than 6')
                self.value = None

            if self.value is None:
                return None

            self.value = value

    def __init__(self, name='', email='', password=''):
        self.name = self.Name(name).value
        self.email = self.Email(email).value
        self.password = self.Password(password).value

    def valid(self):
        if self.name and self.email and self.password:
            return True
        else:
            return False

    def error(self):
        print(self.Name.errors)
        print(self.Email.errors)
        print(self.Password.errors)
