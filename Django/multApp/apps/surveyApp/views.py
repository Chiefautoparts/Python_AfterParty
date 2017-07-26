from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request, 'surveyApp/.html')
def new(request):
	return render(request, 'surveyApp/newSurvey.html')
	#display = 'placeholder for users to add new survey'
	#return HttpResponse(display)


	

def recieve(request):
	if request.POST['submit'] == 'sent':
		if 'counter' not in request.session:
			request.session['counter'] = 0
		request.session['counter'] = request.session['counter'] + 1
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
	else:
		if 'counter' in request.session:
			counter = request.session['counter']
		request.session.clear()
		request.session['counter'] = counter
	return redirect('/display')

def display(request):
	return render(request, 'surveyApp/display.html')