from django.db import models

# Create your models here.


class Auth(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'auth'
        verbose_name = '権限'


class User(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, null=True)
    birth_date = models.DateField(null=True)
    auth = models.ForeignKey(Auth, models.SET_NULL, null=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'ユーザー'

 