from django.shortcuts import render, HttpResponse, redirect 


def index(request):
	return render(request, 'blogs/index.html')


# Create your views here.
