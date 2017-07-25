from __future__ import unicode_literals

from django.db import models
from ..login.models import User
# Create your models here.
class CatManager(models.Manager):
	def addCat(self, postData):
		results = {'status':True, 'errors':[]}
		if not postData['name'] or len(postData['name']) < 1:
			results['status']=False
			results['errors'].append('Your Cat must certainly have a name')
		if not postData['age'] or postData['age']<1:
			results['status']=False
			results['errors'].append('Yes cats don\'t abide to the laws of nature but they must have an age')

		user = User.objects.get(id=postData['user_id'])
		if results['status']:
			try:
				cat = Cat.objects.create(
										name=postData['name'],
										age=postData['age'],
										user_id=user
										)
				cat.save()
			except:
				results['errors'].append('Feline Error: Cat not created')
		return results

	def likeCat(self, postData, user_id):
		results = {'status':True, 'errors':[]}

		try:
			cat = Cat.objects.get(postData['cat_id'])
			user = User.objects.get(id=user_id)
			like = cat.likedcats.add(cat)
			cat.save()
		except:
			results['errors'].append('Feline Error: Cat has not been Liked')
		
		return results


class Cat(models.Model):
	name = models.CharField(max_length=255)
	age = models.IntegerField()
	user_id = models.ForeignKey('login.user', related_name='cats')
	likes = models.ManyToManyField('login.user', related_name='likedCats')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = CatManager()