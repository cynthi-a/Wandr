from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # additional attributes
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username

class Picture(models.Model):
	picture_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128, unique=False)
	description = models.CharField(max_length=200, unique = False)
	picture = models.ImageField(upload_to='profile_images', blank=False)

	def __str__(self):
		return self.picture_id