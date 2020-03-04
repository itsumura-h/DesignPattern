import re


class User:
    class Name:
        value = ''

        def __init__(self, value):
            if len(value) == 0:
                self.value = None

            pattern = re.compile(r'^(\w)+')
            if not pattern.match(value):
                self.value = None

            if len(value) > 50:
                self.value = None

            if self.value is None:
                return None

            self.value = value

    class Email:
        value = ''

        def __init__(self, value):
            if len(value) == 0:
                self.value = None

            pattern = re.compile(r'^(\w)+')
            if not pattern.match(value):
                self.value = None

            if len(value) > 255:
                self.value = None

            pattern = re.compile(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9]+\.[?:\.a-zA-Z0-9]*$")
            if not pattern.match(value):
                self.value = None

            if self.value is None:
                return None

            self.value = value

    def __init__(self, name='', email=''):
        self.name = self.Name(name).value
        self.email = self.Email(email).value

    def valid(self):
        if self.name and self.email:
            return True
        else:
            return False
