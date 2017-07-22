from __future__ import unicode_literals
from datetime import datetime
import re
import bcrypt
from django.db import models

# Create your models here.

class UserManager(models.Manager):
	def regValidate(self, postData):
		status= {'valid':True, 'errors':[], 'user':None}
		if not postData['name'] or len(postData['name']) < 3:
			status['valid']=False
			status['errors'].append('Thats not your real name. Try agian or I will be forced to take action')
		if not postData['username'] or len(postData['username']) < 3:
			status['valid']=False
			status['errors'].append('That username is invalid for TWO reasons. 1. It Sucks. 2. It\'s not long enough.')
		if not postData['email'] or re.match('r(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', postData['email']):
			status['valid']=False
			status['errors'].append('FAKE EMAIL!!!!!')
		if not postData['age'] or postData['age'] < 15:
			status['valid']=False
			status['errors'].append('You are just a kid get out of here')
		if not postData['password'] or len(postData['password']) < 6:
			status['valid']=False
			status['errors'].append('Ok John Podesta how about you pick a better password than "password"')
		if postData['confirmPassword'] != postData['password']:
			status['valid']=False
			status['errors'].append('NOPE!')
		if status['valid'] is False:
			return status

		user = User.objects.filter(username=postData['username'])

		if user:
			status['valid']=False
			status['errors'].append('Registering has Failed.')

		if status['valid']:
			user = User.objects.create(
				name = postData['name'],
				username = postData['username'],
				email = postData['email'],
				age = postData['age'],
				password = (bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
				)
			user.save()
			status['user'] = user
		return status

	def loginValidate(self, postData):
		status = {'valid':True, 'errors':[], 'user':None}
		user = User.objects.filter(username=postData['username'])

		try:
			user[0]
		except IndexError:
			status['valid'] = False
			status['errors'].append('Login infomation is INVALID')

		if user[0]:
			if user[0].password != bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()):
				status['valid']=False
				status['errors'].append('Login Infomations is INVALID')
			else:
				status['user'] = user[0].id
		else:
			status['valid'] = False
		return status

class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	age = models.IntegerField()
	password = models.CharField(max_length=255)
	confirmPassword = models.CharField(max_length=255)
	created_at =  models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id) + ', ' + self.username

	objects = UserManager()