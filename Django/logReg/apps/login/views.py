from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect 
from .models import User
from django.contrib import messages


def index(request):
	
	return render(request, 'login/index.html')

def register(request):
	status = User.objects.registerValidation(request.POST)
	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
	else:
		messages.success(request, 'User createed,  login please')
	request.session['id'] = status['user'].id
	# print request.post['user.first_name']*50
	# print request.post['user.email']*50
	# print request.post['user.password']*50
	return redirect('auth:index')

def login(request):
	status = User.objects.loginValidation(request.POST)
	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
	else:
		request.session['id'] = status['user'].id
		return redirect('auth:success')
	return redirect('/')

def logout(request):
	request.session.clear()
	return redirect('auth:index')

def success(request):
	user = User.objects.get(id=request.session['id'])
	context = {
		'user': user
	}
	
	return render(request, 'login/success.html', context)