from django.conf.urls import url
from . import views

#appname = login 

urlpatterns = [
	url(r'^$', views.index,  name=index),
	url(r'^login$', views.login, name=login),
	url(r'^register$', views.register, name=register),f
	url(r'^user/(?P<user_id>\d+)$', views.showUser, name=display)
] 