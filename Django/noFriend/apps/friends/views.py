from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Friendship, User


def home(request):
	user = User.objects.get(id=request.session.get('id'))
	#friends = Friend.objects.all().order_by('-created_at')[:3]
	context = {
		'user': user,
		
	}
	return render(request, 'friends/friends.html', context)



def add_friend(request, first_name):
	user = User.objects.get(id=request.session('id'))
	Friendship.objects.get_or_create(from_user=request.user, to_user=user)
	return redirect('friends:home')

def show_friends(request, first_name):
	user = User.objects.get(request.session('first_name'))
	friends = user.friendship.filter(to_user__from_user=user)
	context = {
		'user': friends
	}
	return render(request, 'friends/friendpage.html', context)