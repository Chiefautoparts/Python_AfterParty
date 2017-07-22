from __future__ import unicode_literals

from django.db import models

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
		if not postData['email'] or not re.match(r'(^[a-zA_Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', postData['email']):
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
		user = User.objects.filter(alias=postData['alias'])

		if user:
			status['valid']=False
			status['errors'].append('Failed to register')

		if status['valid']:
			try:
				user = User.objects.create(
					name=postData['name'],
					alias=postData['alias'],
					email=postData['emial'],
					password=(bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())))
				user.save()
				status['user'] = user
			except IntegrityError as e:
				status['valid'] = False
				if 'UNIQUE constraint' in e.message:
					status['errors'].append('email is already registered')
				else:
					status['errors'].append(e.messages)
			return results
			




class User(models.Model):
	name=models.CharField(max_length=255)
	alias=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	created_at =  models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()
