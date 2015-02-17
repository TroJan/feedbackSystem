from django.db import models

# Create your models here.
class Review(models.Model):

	def __str__(self):
		return self.name

	name =  models.CharField(max_length=200)
	comment = models.CharField(max_length=1000)
	year = models.CharField(max_length=5)
	addons = models.CharField(max_length=1000)
	rating=models.CharField(max_length=5)
