import logging

from orator import DatabaseManager
from orator import Model
from django.conf import settings

config = {
    # 'mysql': {
    #     'driver': 'mysql',
    #     'database': settings.DATABASES['default']['NAME'],
    #     'host': settings.DATABASES['default']['HOST'],
    #     'user': settings.DATABASES['default']['USER'],
    #     'password': settings.DATABASES['default']['PASSWORD'],
    #     'prefix': '',
    #     'log_queries': True,
    # }
    'sqlite': {
        'driver': 'sqlite',
        'database': settings.DATABASES['default']['NAME'],
        'prefix': '',
        'log_queries': False,
    }
}


db = DatabaseManager(config)
Model.set_connection_resolver(db)


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
    # __timestamps__ = False


class MicroPost(Model):
    __table__ = 'microposts'
    __timestamps__ = False
