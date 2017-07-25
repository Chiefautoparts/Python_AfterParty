from __future__ import unicode_literals
import bcrypt
import re
from django.db import models, IntegrityError

# Create your models here.
class UserManager(models.Manager):
	def registerUser(self, postData):
		results={'status':True, 'errors':[], 'user':None}
		if not len(postData['fName']) < 3:
			results['status']=False
			results['errors'].append('Fake First Name')
		if not len(postData['lName']) < 3:
			results['status']=False
			results['errors'].append('That last name is about as credible as cnn\'s reporting')
		if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", postData['email']):
			results['status']= False
			results['errors'].append('that email be whack yo')
		if not len(postData['password']) < 8:
			results['status']=False
			results['errors'].append('Putin thanks you for such a simple password')
		if postData['confirmPassword'] != postData['password']:
			results['status']=False
			results['errors'].append('no match')

		user = User.objects.filter(email=postData['email'])

		if results['status']:
			try:
				user = User.objects.create(
											fName=postData['fName'],
											lName=postData['lName'], 
											email=postData['email'], 
											password=(bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())))
				
				user.save()
				results['user']=user

			except IntegrityError as e:
				results['status']=False
				if 'UNIQUE constraint'in e.message:
					results['errors'].append('email already in system')
				else:
					results['errors'].append(e.message)
		return results

	def loginVal(self, postData):
		results = {'status':True, 'errors':[], 'user':None}
		try:
			user = User.objects.get(email=postData['email'])
			if user.password == bcrypt.hashpw(postData['password'].encode(), user.password.encode()):
				pass
			else:
				raise Exception()
		except Exception as e:
			results['status']=False
			results['errors'].append('incorrect Username or password')

		if results['status']:
			results['user'] = user
		return results


class User(models.Model):
	fName = models.CharField(max_length=255)
	lName = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()