from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length = 200)
	phone = models.CharField(max_length = 200)
	birthday = models.DateField("Birthday")
	adress = models.CharField(max_length = 200)
	
	def __str__(self):
		return self.name

#python manage.py makemigrations.polls
#python manage.py migrate (creat 0001)	

