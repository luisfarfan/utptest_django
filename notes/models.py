from django.contrib.auth.models import User
from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    date_create = models.DateTimeField(auto_now_add=True)
    date_edited= models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
