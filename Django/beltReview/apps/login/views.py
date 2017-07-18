from django.shortcuts import render, redirect
from .models import User
from django.contrib.messages import messages
# Create your views here.
def index(request):
	#print '*'*100
	if request.session.get('id'):
		return redirect('/showUser')
	return render(request, 'login/index.html')

def login(request):
	#print 'login'*50
	status = User.objects.validLogin(request.POST)
	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
		return redirect('/')
	else:
		user = User.objects.get(id=status['user'])
		request.session['id'] = user.id
	return redirect('/showUser')


def register(request):
	#print 'register'*50
	status = User.objects.validRegister(request.POST)
	if not status['valid']:
		for error in status['errors']:
			messages.error(request, error)
		return redirect('/')
	request.session['id'] = status['user'].id
	return redirect('/showUser')

def showUser(requests):
	user = User.objects.get(id=request.session['id'])
	context = {
		'user': user
	}
	return render(request, 'login/user<id>.html', context)