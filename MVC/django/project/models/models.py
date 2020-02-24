from django.db import models

# Create your models here.


class User(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'
        verbose_name = 'ユーザー'


class MicroPost(models.Model):
    def __str__(self):
        return self.content

    content = models.TextField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'microposts'
        verbose_name = '投稿'
