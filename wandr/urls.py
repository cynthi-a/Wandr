from django.conf.urls import url
from wandr import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
]