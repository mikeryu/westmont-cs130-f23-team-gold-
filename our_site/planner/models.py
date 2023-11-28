from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    roles = models.ManyToManyField("Role", related_name="fulfilled_by")


class Event(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="events")
    name = models.CharField(max_length=30)
    date = models.DateField()
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    invitees = models.ManyToManyField(Profile, related_name="invitations")


class Role(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="roles")
    amount = models.IntegerField()
