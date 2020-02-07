import os, logging
import environ

from orator import DatabaseManager, Schema, Model
from django.conf import settings

env = environ.Env()

try:
    settings.configure()
except:
    pass

if settings.DJANGO_ENV == 'test':
    config = {
        'default': 'database',
        'database': {
            'driver': 'postgres',
            'host': settings.DATABASES['default']['HOST'],
            'database': settings.DATABASES['default']['TEST']['NAME'],
            'port': settings.DATABASES['default']['PORT'],
            'user': settings.DATABASES['default']['USER'],
            'password': settings.DATABASES['default']['PASSWORD'],
            'log_queries': False,
        }
    }
else:
    config = {
        'default': 'database',
        'database': {
            'driver': 'postgres',
            'host': settings.DATABASES['default']['HOST'],
            'database': settings.DATABASES['default']['NAME'],
            'port': settings.DATABASES['default']['PORT'],
            'user': settings.DATABASES['default']['USER'],
            'password': settings.DATABASES['default']['PASSWORD'],
            'log_queries': False,
        }
    }

db = DatabaseManager(config)
model = Model.set_connection_resolver(db)


logger = logging.getLogger('orator.connection.queries')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    'It took %(elapsed_time)sms to execute the query %(query)s'
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger.addHandler(handler)

class User(Model):
    __table__ = 'users'