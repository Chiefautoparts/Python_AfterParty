from django.shortcuts import render, redirect
from .models import User

def index(request):
	print '*'*100
	return render(request, 'userApp/index.html')

def new(request):
	print 'NEW'*50
	return render(request, 'userApp/new.html')

def edit(request):
	print 'edit'*50

def show(request):
	request.session['fName'] = request.POST['fName']
	request.session['lName'] = request.POST['lName']
	request.session['email'] = request.POST['email']
	full_name = request.session['fName'] + ' ' + request.session['lName']

	return render(request, '')
	print 'show'*50

def create(request):
	print 'create'*50
	if request.method == 'POST':
		fName = request.POST['fName']
		lName = request.POST['lName']
		email = request.POST['email']
		return redirect('/userApp/show')

def destroy(request):
	print 'destroy'*50

def update(request):
	print 'update'*50