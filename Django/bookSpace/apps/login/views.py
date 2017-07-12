from django.shortcuts import render, HttpResponse, redirect


def index(request):
	return render(request, 'login/index.html')

def register(request):
	if request.method == 'POST':
		request.session['username'] = request.POST['username']
		request.session['email'] = request.POST['email']
		request.session['age'] = request.POST['age']
		request.session['fName'] = request.POST['fName']
		request.session['lName'] = request.POST['lName']
		return redirect('/home')
	else:
		errors = 'one or more pieces of information is incorrect please check'
		request.session['errors'] = errors
		return redirect('/')

def home(request):
	return render(request, 'login/home.html')

# Create your views here.
