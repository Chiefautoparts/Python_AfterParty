from __future__ import unicode_literals
import re
import bcrypt

from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def validRegister(self, postData):
		status = {'valid': True, 'errors': [], 'user': None}
		if not postData['name'] or len(postData['name']) < 3:
			status['valid'] = False
			status['errors'].append('name must be longer. FAKE NEWS!!!')
		if not postData['alias'] or len(postData['all']) < 4:
			status['valid'] = False
			status['errors'].append('username is too short')
		if not postData['email'] == re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$)'): 
			status['valid'] = False
			status['errors'].append('enter a valid email ')
		if not postData['password'] or len(postData['password']) < 6:
			status['valid'] = False
			status['errors'].append('Password is not long enough')
		if postData['confirm_password'] != postData['password']:
			status['valid'] = False
			status['errors'].append('passwords do not match')
		if status['valid'] is False:
			return status

		user = User.objects.fitler(name=postData['name'])

		if user:
			status['valid'] =False
			status['errors'].append('Failed to register, try it again champ')

		if status['valid']:
			password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
			user = User.objects.create(
							name = postData['name'],
							alias = postData['alias'],
							email = postData['email'],
							password = password
					)
			status['user'] = user
		return status

	def validLogin(self, postData):
		status = {'valid':True, 'errors':[], 'user': None}
		user = User.objects.fitler(name=postData['name'])
		try:
			user[0]
		except IndexError:
			status['valid'] =False
			status['errors'].append('No account exist, YOU HAVE FAILED')

		if user[0]:
			if user[0].password != bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()):
				status['valid'] = False
				status['errors'].append('Password doesnt match, DUMBASS')
			else:
				status['user'] = user[0].id
		else:
			status['valid'] = False
		return logged



class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id) + ', ' + self.alias

	objects = UserManager()