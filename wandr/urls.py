from django.conf.urls import url
from wandr import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^picture_overview/$', views.picture_overview, name='picture_overview'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^add_picture/$', views.add_picture, name='add_picture'),
    url(r'^add_picture_success/$', views.add_picture_success, name='add_picture_success'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.user_profile_view, name='user_profile'),
    url(r'^profile/(?P<user_id>[0-9]+)/upload_profile_picture/$', views.upload_profile_picture, name='upload_p_picture'),
    url(r'^profile/(?P<user_id>[0-9]+)/upload_cover_photo/$', views.upload_cover_photo, name='upload_cover_photo'),
    url(r'^profile/(?P<user_id>[0-9]+)/update_profile/$', views.update_profile, name='update_profile'),
    url(r'^profile/(?P<user_id>[0-9]+)/add/(?P<picture_id>[0-9]+)$', views.add_to_tgl, name='add_to_tgl'),
    url(r'^profile/(?P<user_id>[0-9]+)/remove_tgl/(?P<picture_id>[0-9]+)$', views.remove_from_tgl, name='remove_from_tgl'),
    url(r'^profile/(?P<user_id>[0-9]+)/remove_hbl/(?P<picture_id>[0-9]+)$', views.remove_from_hbl, name='remove_from_hbl'),

    url(r'^profile/(?P<user_id>[0-9]+)/like_picture/(?P<picture_id>[0-9]+)$', views.like_picture, name='like_picture'),
]