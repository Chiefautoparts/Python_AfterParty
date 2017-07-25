from django.shortcuts import render, redirect
from .models import User, Cat
from django.contrib import messages

def userPage(request):
	user = User.objects.get(id=request.session.get('id'))
	cats = Cat.objects.all().order_by('-created_at')[:5]
	context = {
		'user': user,
		'cats': cats,
	}
	return render(request, 'katBook/userPage.html', context)

def addCat(request):
	if request.POST:
		results = Cat.objects.addCat(request.POST)
		if results:
			messages.info(request, 'Cat added')
		else:
			for error in results:
				messages.error(request, error)
			return redirect('katBook:addCat')
		return  redirect('katBook:userPage')
	user = User.objects.get(id=request.session.get('id'))
	context = {
		'user': user,
	}
	return render(request, 'katBook/addCat.html', context)

def likeCat(request):
	if request.POST:
		results = Cat.objects.likeCat(request.POST, request.session['id'])
		if results:
			messages.info(request, 'Cat Liked!!')
		else:
			for error in results:
				messages.error(request, error)
		return redirect('katBook:userPage')
