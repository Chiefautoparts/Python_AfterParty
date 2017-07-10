from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	show = 'placeholder to display all surveys created'
	return HttpResponse(show)

def new(request):
	display = 'placeholder for users to add new survey'
	return HttpResponse(display)