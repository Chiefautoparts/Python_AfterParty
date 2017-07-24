from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def index(request):
	return render(request, 'userLogin/index.html')
	print '*' * 250
	
def register(request):
	print '**register**'*100
	status = User.objects.registerUser(request.POST)

	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
	else:
		messages.success(request, 'User created, now login.')
	
	return redirect('/')

def login(request):
	print '**login**'*100
	status = User.objects.loginUser(request.POST)

	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
	else:
		request.session['id'] = status['user'].id
		return redirect('/showUser')
	return redirect('/')

def showUser(request, id):
	print '**showUser**'*100
	if not request.session.get('id'):
		messages.error(request, 'please login first')
		return redirect('/')
	user = User.objects.get(id=id)
	context = {
		'user': user
	}
	return render(request, 'userLogin/displayUser.html', context)