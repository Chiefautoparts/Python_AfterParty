from django.shortcuts import render, HttpResponse, redirect
import random


# Create your views here.
def  index(request):
	return render(request, 'wordGen/index.html')

def generator(request):
	if 'counter' in request.session:
		request.session['counter'] += 1
	else:
		request.session['counter'] = 1 
	word = ''
	chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for times in range(0,14):
		word = word + str(random.choice(chars))
	words = {
		'randomWord': word
	}
	return render(request, 'wordGen/index.html', words)
	


	# return render(request, 'wordGen/index.htm')