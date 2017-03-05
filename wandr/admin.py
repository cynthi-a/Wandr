from django.contrib import admin
from wandr.models import UserProfile, Picture, HaveBeenList

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Picture)
admin.site.register(HaveBeenList)