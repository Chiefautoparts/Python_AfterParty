from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
	
	return render(request, 'timedisplay/index.html')


	#% now "jS F Y H:i" %}