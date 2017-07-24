from __future__ import unicode_literals
import re
import bcrypt
from django.db import models, IntegrityError

# Create your models here.
class UserManager(models.Manager):
	def registerValidation(request, postData):
		status = {'valid': True, 'errors':[], 'user': None}
		if not postData['first_name'] or len(postData['first_name']) < 2:
			status['valid'] = False
			status['errors'].append('First name must be longer than 2 characters')
		if not postData['last_name'] or len(postData['last_name']) < 2:
			status['valid'] = False
			status['errors'].append('Last name must be longer than 2 characters')
		if not postData['email'] or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", postData['email']):
			status['valid'] = False
			status['errors'].append('Invalid email')
		if not postData['password'] or len(postData['password']) < 8:
			status['valid'] = False
			status['errors'].append('Password must be at least 8 characters long')
		if postData['confirm_password'] != postData['password']:
			status['valid'] = False
			status['errors'].append('Passwords to not match')
		
		user = User.objects.filter(email= postData['email'])
		
		if status['valid']:
			try:
				user = User.objects.create(
					first_name = postData['first_name'],
					last_name = postData['last_name'],
					email = postData['email'],
					password = (bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
					)
				print user
				user.save()
				status['user'] = user
			except IntegrityError as e:
				status['valid'] = False
				if 'UNIQUE constraint' in e.message:
					status['errprs'].append('email already used')
				else:
					status['errors'].append(e.message)
		return status

	def loginValidation(self, postData):
		status = {'valid':True, 'errors': [], 'user': None}
		user = User.objects.filter(email=postData['email'])
		try: 
			user[0]
		except IndexError:
			status['valid']=False
			status['errors'].append('Your login has failed')

		if user[0]:
			if user[0].password != bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()):
				status['valid']=False
				status['errors'].append('login failed')
			else:
				status['user'] = user[0].id
		else:
			status['valid']=False
		return status





		# user = User.objects.get(email=postData['email'])
		# if user.password == bcrypt.haspw(postData['password'].encode, user.password.encode()):
		# 	return status
		# else:
		# 	status['valid'] = False
		# 	status['errors'].append('Incorrect username or password')

		# if status['valid']:
		# 	status['user'] = user
		# return status 

		# except IndexError:
		# 	status['valid'] = False
		# 	status['errors'].append('No Account found with the information provided. GO REGISTER')

		# if user[0]:
		# 	if user[0].password != bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()):
		# 		status['valid'] = False
		# 		status['errors'].append('Password is WRONG')
		# 	else:
		# 		status['user'] = user[0].id
		# else:
		# 	status['valid'] = False
		# return status


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id) + ", " + self.first_name

	objects  = UserManager()