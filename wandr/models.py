from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class HaveBeenList(models.Model):
    # list_id = models.AutoField(primary_key=True)
    belongs_to = models.OneToOneField(User)

    total_likes = models.IntegerField(default=0)


    def __unicode__(self):
        return str(self.pk)


def create_hbl(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
        have_been_list = HaveBeenList.objects.create(belongs_to=kwargs['instance'])
        to_go_list = ToGoList.objects.create(belongs_to=kwargs['instance'])

post_save.connect(create_hbl, sender=User)


class ToGoList(models.Model):
    belongs_to = models.OneToOneField(User)

    def __unicode__(self):
        return str(self.pk)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # additional attributes
    picture = models.ImageField(upload_to='profile_images', blank=True)
    cover_photo = models.ImageField(upload_to='cover_photos', blank=True)
    bio = models.TextField(max_length=600, blank=True)

    def __unicode__(self):
        return str(self.user.username)


class Picture(models.Model):
    picture_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=False)
    description = models.CharField(max_length=200, unique=False, default = 'unknown')
    picture = models.ImageField(upload_to='travel_images', blank=False)
    likes = models.IntegerField(default=0)
    have_been_list = models.ForeignKey(HaveBeenList, on_delete=models.CASCADE)
    to_go_list = models.ManyToManyField(ToGoList)
    location = models.CharField(max_length=128, unique=False)

    def __unicode__(self):
        return 'Name: ' + str(self.picture_id) + ' --- ID: ' + str(self.picture_id)
