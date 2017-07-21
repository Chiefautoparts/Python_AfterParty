from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages



def index(request):
	
	return render(request, 'login/home.html')

def register(request):
	status = User.objects.regValidate(request.POST)
	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
		return redirect('/')
	request.session['id'] = status['user'].id
	return redirect('/show')
	print '*REGISTER*' * 100

def login(request):
	status=User.objects.loginValidate(request.POST)
	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
		return redirect('/')
	request.session['id'] = status['user'].id
	return redirect('/show')
	print '**LOGIN**' *250

def show(request):
	user = User.objects.get(id=request.session['id'])
	context = {
		'user': user,
	}
	return render(request, 'login/mainPage.html', context)