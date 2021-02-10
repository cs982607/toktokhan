from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email    = models.EmailField(max_length=50)
    password = models.CharField(max_length=200)

    class Meta:
        db_table = 'users'

