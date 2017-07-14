from django.shortcuts import render, HttpResponse, redirect 

def bookindex(request):
	return render(request, 'book_author/book.html')

# Create your views here.
