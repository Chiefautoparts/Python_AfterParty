from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages


def index(request):
	print '**index**'*100

	return render(request, 'catLogin/index.html')

def register(request):
	results = User.objects.registerUser(request.POST)
	if not results['status']:
		for error in results['errors']:
			messages.error(request, error)
	else:
		messages.success(request, 'User register, time to log in to dis beeeeesh')
	return redirect('/login')

def login(request):
	
	results = User.objects.loginVal(request.POST)
	if not results['status']:
		for error in results['errors']:
			messages.error(request, error)
	else:
		request.session['id'] = results['user'].id
		return redirect('/showUser')
	return redirect('/')

def showUser(request):
	user = User.objects.get(id=request.session['id'])
	context = {
		'user': user
	}
	
	return render(request, 'catLogin/user.html', context)


# Create your views here.
