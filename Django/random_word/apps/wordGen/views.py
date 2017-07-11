from django.shortcuts import render, HttpResponse, redirect
import random


# Create your views here.
def  index(request):
	word = random.randrange(a,z)


	return render(request, 'wordGen/index.htm')