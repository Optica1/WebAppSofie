from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class UserDetails(models.Model):
    user = models.OneToOneField(User)
    phonenumber = models.CharField(max_length=12)

class Client(models.Model):
    voornaam = models.CharField(max_length=60)
    achternaam = models.CharField(max_length=60)

class Aboutpage(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField(max_length=1024)
