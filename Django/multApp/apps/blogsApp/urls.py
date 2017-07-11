from django.conf.urls import url
from .  import views

urlpatterns = [
	url(r'^/$', views.index),
	url(r'^/new$', views.new),
	url(r'^/create$', views.create),
	url(r'^/{{number}}$', views.show),
	url(r'^/{{number}}/edit$', views.edit),
	url(r'^/{{number}}/delete$', views.destroy),
] 