from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):
	user_name=models.CharField(max_length=30)
	title=models.CharField(max_length=50)
	content=models.TextField()
''''class User(models.User):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	no_of_blogs=models.IntegerField()

	def __str__():
		return self.first_name'''

		
