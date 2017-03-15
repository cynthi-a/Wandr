from django.contrib import admin
from wandr.models import UserProfile, Picture, HaveBeenList, ToGoList

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Picture)
admin.site.register(HaveBeenList)
admin.site.register(ToGoList)