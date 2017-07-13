from django.shortcuts import render, HttpResponse, redirect 
from datetime import datetime
import random

def index(request):
	if 'currentGold' not in request.session:
		request.session['currentGold'] = 0

	if 'activities' not in request.session:
		request.session['activities'] = ''
	return render(request, 'ninjaApp/index.html')

def process_money(request):
	loc = request.POST['location']
	currentGold = request.session['currentGold']
	moneys = 0
	if loc == "farm":
		moneys = random.randint(10,20)
	elif loc == "cave":
		moneys = random.randint(5,10)
	elif loc == "house":
		moneys = random.randint(2,5)
	elif loc == "casino":
		moneys = random.randint(-50,50)
	else:
		request.session['currentGold'] = 0
	

	hammerTime = datetime.now()
	powerTools = 'At ' + str(hammerTime) + ' you acquired ' +  str(moneys) + ' more Gold ' + ' from the ' + loc
	request.session['currentGold'] += moneys
	request.session['activities'] = powerTools 
	return redirect('/')