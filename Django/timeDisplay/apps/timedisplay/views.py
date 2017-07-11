from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
	request.session['now'] = datetime.datetime.now()
	return render(request, 'timedisplay/index.html')


	#% now "jS F Y H:i" %}