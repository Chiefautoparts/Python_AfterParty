from django.shortcuts import render, HttpResponse, redirect 

def index(request):
	print '*'*100
	return render(request, 'bookAuthor/index.html')

# Create your views here.
