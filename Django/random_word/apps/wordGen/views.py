from django.shortcuts import render, HttpResponse, redirect
import random


# Create your views here.
def  index(request):
	chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	word = ''.join(random.choice(chars)for _ in range(10))
	request.session['counter'] = 0
	counter += 1


	return render(request, 'wordGen/index.htm')