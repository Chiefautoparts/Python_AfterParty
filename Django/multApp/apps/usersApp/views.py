from django.shortcuts import render, HttpResponse

# Create your views here.
def register(request):
	display = 'placeholder for users to create a new user record'
	return HttpRespone(display)

def login(request):
	display = 'placeholder for users to login'
	return HttpResponse(display)

def users(request):
	display = 'placeholder to later display all the list of users'
	return HttpResponse(display)