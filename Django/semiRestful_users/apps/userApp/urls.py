from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='user_home'),
	url(r'^userApp/new$', views.new, name='user_new'),
	url(r'^userApp/<id>/edit$', views.edit, name='user_edit'),
	url(r'^userApp/<id>$', views.show, name='user_show'),
	url(r'^userApp/create$', views.create, name='user_create'),
	# request.POST ^
	url(r'^userApp/<id>/destroy$', views.destroy, name='user_destroy'),
	url(r'^userApp/update/<id>$', views.update, name='user_update'),
	#request.POST ^ 
	
]