from django.conf.urls import url 
from . import views 

urlpatterns = [
	url(r'^/register$', views.register, name='registerUser'),
	url(r'^/login$', views.login, name='userLogin'),
	url(r'^/users/new$', views.register, name='createUser'),
	url(r'^/users$', views.display, name='display_users')
]