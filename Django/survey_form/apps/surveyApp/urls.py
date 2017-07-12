from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^recieve$', views.recieve),
	url(r'^display$', views.display),
	#url(r'^returnHome$', views.backup)
]