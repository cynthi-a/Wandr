from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # additional attributes
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username