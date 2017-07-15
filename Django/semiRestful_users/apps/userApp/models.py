from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Model):
	def validUser(self, postData):
		errors = {}
		if not postData['fName'] or len(postData['fNamer']) < 2:
			errors['fName'] = "first name not valid. try again idiot"
		if not postData['lName'] or len(postData['lname']) < 2:
			errors['lName'] = 'last name not valid. get it right'
		if not postData['email'] or len(postData['email']) < 4:
			errors['email'] = 'Emali invalid. NO FAKE EMAILS'
		return errors
		
class User(models.Model):
	fName = models.CharField(max_length=255)
	lName = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at =  models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()