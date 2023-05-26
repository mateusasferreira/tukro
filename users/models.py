from django.contrib.auth.models import AbstractUser, User
from django.db import models

class User(AbstractUser):
    location = models.CharField(max_length=100, blank=False)
    birth_date = models.DateField(blank=False)
