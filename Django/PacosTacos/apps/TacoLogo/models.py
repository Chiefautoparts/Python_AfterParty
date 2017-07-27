from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Taco(models.Model):
	meat = models.CharField(max_length=255)
	toppings = models.CharField(max_length=255)
	spice_level = models.CharField(max_length=255)

class User(models.Model):
	name = models.CharField(max_length=255)
	toppings = models.ForeignKey(Taco, related_name='toppings')