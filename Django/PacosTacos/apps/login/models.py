from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

class ChumpManager(models.Manager):
	status={'valid':True, 'errors':[], 'user':None}
	if not postData['fName'] or len(postData['fName']) < 2:
		status['valid']=False
		status['errors'].append('We don\'t want people with that first name on this site')
	if not postData['lName'] or len(postData['lName']) < 2:
		status['valid']=False
		status['errors'].append('That last name is different and it scares me so it\'s wrong')
	if not postData['password'] or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", postData['email']):
		status['valid']=False
		status['errors'].append('Jesus says that email is a temptation from the devil to lead us away from the good path brother')
	if not postData['password'] or len(postData['password']) < 6:
		status['valid']=False
		status['errors'].append('That password is weak as shit. Just leave don\'t even come back. I hate you')
	if postData['confirmPassword'] != postData['password']:
		status['valid']=False
		status['errors'].append('hctam ton od sdrowssap. (place computer infront of mirror to read error message)')




class Chump(models.Model):
	fName = models.CharField(max_length=255)
	lName = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at =  models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = ChumpManager()