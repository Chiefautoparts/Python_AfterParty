from django.shortcuts import render, redirect 

def index(request):
	return render(request, 'login/index.html')

# Create your views here.
