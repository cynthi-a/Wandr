from django.conf.urls import url
from wandr import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^add_picture/$', views.add_picture, name='add_picture'),
    
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.user_profile_view, name='user_profile'),
    url(r'^profile/(?P<user_id>[0-9]+)/upload_profile_picture/$', views.upload_profile_picture, name='upload_p_picture'),
    url(r'^profile/(?P<user_id>[0-9]+)/upload_cover_photo/$', views.upload_cover_photo, name='upload_cover_photo'),
]