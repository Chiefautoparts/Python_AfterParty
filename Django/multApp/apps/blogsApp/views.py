from django.shortcuts import render, HttpResponse, redirect


def index(request):
	text = 'placeholder to later display all the list of blogs'
	return HttpResponse(text)

def new(request):
	holder = 'placeholder to display a new form to create a new blog'
	return HttpResponse(holder)

def create(request):
	return redirect('/blogs')

def show(request):
	placeholder = 'placeholder to display blog {{number}}'
	return HttpResponse(placeholder)

def edit(request):
	phedit = 'palceholder to edit blog {{number}}'
	return HttpResponse(phedit)

def destroy(request):
	return redirect('/blogs')


# Create your views here.
