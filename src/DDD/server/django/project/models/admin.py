from django.contrib import admin
from .models import (
    Auth,
    User
)

# Register your models here.

admin.site.register(Auth),
admin.site.register(User)
