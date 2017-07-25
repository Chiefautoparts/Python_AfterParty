from __future__ import unicode_literals

from django.db import models
from ..login.models import User

class Friendship(models.Model):
	from_user = models.ForeignKey(User, related_name="from_user")
	to_user = models.ForeignKey(User, related_name="to_user")
	
	