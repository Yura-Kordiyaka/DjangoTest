from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('user.CustomUser', related_name='teams', on_delete=models.SET_NULL, null=True, blank=True)
    members = models.ManyToManyField('user.CustomUser', related_name='teams_members', blank=True)
