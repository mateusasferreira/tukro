from django.db import models

from users.models import User

class Community(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(blank=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    members = models.ManyToManyField(User, related_name='members')
