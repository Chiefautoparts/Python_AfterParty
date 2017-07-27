from django.shortcuts import render, HttpResponse, redirect 

def index(request):
	print '*'*100
	return render(request, 'bookAuthor/index.html')
def register(request):
	results = User.objects.registerUser(request.POST)
	if not result['status']:
		for errors in results['errors']:
			messages.errors(request, errors)
		else:
			messages.success(request, 'You have registered, proceed to login')
	request.session['id']=results['user'].id
	print user.id
	return redirect('/userPage')


# Create your views here.
