from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

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
