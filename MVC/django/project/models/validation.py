import re
from models.orator import User as DbUser
from cerberus import Validator

def email_unique(field, value, error):
    if DbUser.where('email', value).count() > 0:
        error(field, "Must be unique")


class User:
    def __init__(self, name='', email = '', password=''):
        self.name = name
        self.email = email
        self.password = password

    def valid(self):
        schema = {
            'name': {
                'required': True,
                'empty': False,
                'maxlength': 50
            },
            'email': {
                'required': True,
                'empty': False,
                'regex': "\A[\w+\-.]+@[a-zA-Z\d\-]+(\.[a-zA-Z\d\-]+)*\.[a-zA-Z]+\Z",
                'maxlength': 255,
                'validator': email_unique
            },
            'password': {
                'required': True,
                'empty': False,
                'minlength': 6,
            }
        }

        v = Validator(schema)
        result = v.validate({
            'name': self.name,
            'email': self.email,
            'password': self.password
        })
        # if not result:
        #     print(v.errors)
        return result
