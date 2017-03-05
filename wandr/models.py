from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class HaveBeenList(models.Model):
    list_id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return str(self.list_id)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # additional attributes
    picture = models.ImageField(upload_to='profile_images', blank=True)
    have_been_list = models.ForeignKey(HaveBeenList)

    def __unicode__(self):
        return str(self.user.username)


class Picture(models.Model):
    picture_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=False)
    description = models.CharField(max_length=200, unique=False)
    picture = models.ImageField(upload_to='travel_images', blank=False)
    likes = models.IntegerField(default=0)
#    have_been_list = models.ForeignKey(HaveBeenList, on_delete=models.CASCADE)

    def __unicode__(self):
        return 'Name: ' + str(self.picture_id) + ' --- ID: ' + str(self.picture_id)
