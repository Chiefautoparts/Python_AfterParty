from django.conf.urls import url
from .  import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^/new$', views.new, name='new'),
	url(r'^/create$', views.create, name='create'),
	url(r'^/update$', views.update, name='update'),
	url(r'^/{{number}}$', views.show, name='show'),
	url(r'^/{{number}}/edit$', views.edit, name='edit'),
	url(r'^/{{number}}/delete$', views.destroy, name='destroy'),
] 