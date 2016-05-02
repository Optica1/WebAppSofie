from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class UserDetails(models.Model):
    user = models.OneToOneField(User)
    phonenumber = models.CharField(max_length=12)
