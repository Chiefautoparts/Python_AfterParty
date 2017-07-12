from django.shortcuts import render, HttpResponse, redirect 
import random

def index(request):
	return render(request, 'ninjaApp/index.html', moneys)

def process(request):
	farmGold = randrange(10,20)
	caveGold = randrange(5, 10)
	houseGold = randrange(2, 5)
	casinoGold = randrange(0, 50)
	return redirect('/submit')

def submit(request):
	golds = ''
	if request.method == 'POST':
		if submitFarm:
			goldsF = golds + str(farmGold)
		elif submitCave:
			goldsC = golds + str(caveGold)
		elif submitHouse:
			goldsH = golds + str(houseGold)
		else submitCasion:
			goldsG = golds + str(casinoGold)
		moneys = {
			'acquiredCurrency': goldsF,
			'hustledCurrency': goldsC,
			'gotMoney': goldsH,
			'flippedChickens': goldsG
		}
	return redirect('/')



	



