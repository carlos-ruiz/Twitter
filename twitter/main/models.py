from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    name = models.CharField(max_length=100, blank=True)
    birthday = models.DateField(null=True)
    location = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=140, blank=True)
    private = models.BooleanField()

class Tweet(models.Model):
    owner = models.ForeignKey(UserProfile)
    status = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)
