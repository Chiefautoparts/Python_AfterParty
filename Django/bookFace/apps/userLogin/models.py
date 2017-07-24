from __future__ import unicode_literals

from django.db import models, IntegrityError
import bcrypt
import re

# Create your models here.
class UserManager(models.Manager):
	def registerUser(self, postData):
		status = {'valid': True, 'errors':[], 'user':None}
		if not postData['name']:
			status['valid']=False
			status['errors'].append('Name cannot be left blank')
		if not postData['alias']:
			status['valid']=False
			status['errors'].append('Please proviide an online alias for yout account')
		if not postData['email'] or postData['email'] != re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', postData['email']):
			status['valid']=False
			status['errors'].append('Email is invalid')
		if not postData['password'] or len(postData['password'])<6:
			status['valid']=False
			status['errors'].append('Password must be a minimum of 6 characters.... Learn to count')
		if postData['confirmPassword'] != postData['password']:
			status['valid']=False
			status['errors'].append('Get out og here Putin go hack something else. MAKE YOUR PASSWORDS MATCH AGAIN')
		if status['valid'] is False:
			return status
		
		user = User.objects.get(alias=postData['alias'])
		if status['valid']:
			
				user = User.objects.create(
					name=postData['name'],
					alias=postData['alias'],
					email=postData['email'],
					password=(bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())))
				user.save()
				status['user'] = user
		else:
			status['errors'].append('registration has failed')
		return status
			
	def loginUser(self, postData):
		status={'valid': True, 'errors': [], 'user': None}
		try:
			user = User.objects.get(alias=postData['<alias></alias>'])
			if user.password == bcrypt.hashpw(postData['password'].encode(), user.password.encode()):
				pass
			else:
				raise Exception()
		except Exception as e:
			status['valid']=False
			status['errors'].append('Login failed try again')
		
		if status['valid']:
			status['user']=user
		return status

class User(models.Model):
	name=models.CharField(max_length=255)
	alias=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	created_at =  models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

	def __str__(self):
		return str(self.id) + ":" + self.name + "\\" + self.alias + " - " + self.email + " - " + "Created: " + str(self.created_at)

