from django.db import models


class Users(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
