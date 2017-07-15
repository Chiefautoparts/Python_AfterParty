from django.conf.urls import url
from .  import views

urlpatterns = [
	url(r'^/$', views.index, name='blog_index'),
	url(r'^/new$', views.new, name='blog_new'),
	url(r'^/create$', views.create, name='blog_create'),
	url(r'^/update$', views.update, name='blog_update'),
	url(r'^/{{number}}$', views.show, name='blog_show'),
	url(r'^/{{number}}/edit$', views.edit, name='blog_edit'),
	url(r'^/{{number}}/delete$', views.destroy, name='blog_destroy'),
] 