from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class UserManager(models.Manager):
# 	def validateregister(self, postData):
# 		results = {'status': True, 'error': [], 'user': None}
# 		if not postData['username'] or len(postData['username']) < 3:
# 			results['error'].append("username must be longer than 3 characters")
# 			resutls['status'] = False
# 		if not postData['password'] or len(postData['password']) < 6:
# 			results['error'].append('password must be atleast 6 charaters')
# 			results['status'] = False
# 		if not postData['email'] or len(postData['email'])
# 			resutls['error'].append()
class User(models.Model):
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	age = models.DateField()
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id) + ", " + self.username