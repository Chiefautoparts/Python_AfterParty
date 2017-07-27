from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^userPage$', views.userPage, name='userPage'),
	url(r'^addCat$', views.addCat, name='addCat'),
	url(r'^likeCat$', views.likeCat, name='likeCat'),
]