from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse 
from .models import Blog


def index(request):
	text = 'placeholder to later display all the list of blogs'
	return HttpResponse(text)

def new(request):
	holder = 'placeholder to display a new form to create a new blog'

	return HttpResponse(holder)

def create(request):
	if request.method == 'POST':
		print request.POST
		print request.POST['name']
		print request.POST['desc']
		request.session['name'] = "test"
		return redirect(reverse('blog_index'))
	else:
		return redirect(reverse("blog_index"))

def show(request):
	placeholder = 'placeholder to display blog {{number}}'
	return HttpResponse(placeholder)

def update(request):
	errors = Blog.objects.basic_validators(request.Post)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.errors(request, error, extra_tags=tag)
			return redirect(reverse('blog_edit'+id))
		else:
			blog = Blog.objects.get(id = id)
			blog.name = request.POST['name']
			blog.desc = request.POST['desc']
			blog.save()
			return redirect(reverse('blog_show'))
def edit(request):
	phedit = 'palceholder to edit blog {{number}}'
	return HttpResponse(phedit)

def destroy(request):
	return redirect(reverse('blogs_show'))


# Create your views here.
