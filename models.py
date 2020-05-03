from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




# Create your models here.

class Customer(models.Model):
	customer_id=models.AutoField(primary_key=True)
	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	location=models.CharField(max_length=20)
	phone_number=models.IntegerField()
	email_id=models.CharField(max_length=30)

def __unicode__(self):
	return self.first_name

class Delivery_Person(models.Model):
	delivery_id=models.AutoField(primary_key=True)
	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	phone_number=models.IntegerField()
	rating=models.DecimalField(max_digits=2,decimal_places=2, default='0')
	email_id=models.CharField(max_length=30)

def __str__(self):
	return self.first_name	

class Restaurant(models.Model):
	restaurant_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	phone_number=models.IntegerField()
	location=models.CharField(max_length=50)
	RCHOICES=[
	('One','1'),
	('Two','2'),
	('Three','3'),
	('Four','4'),
	('Five','5')]
	rating=models.CharField(default=0, choices=RCHOICES,max_length=10)
	logo=models.ImageField(upload_to='restaurant_logo/', blank=False)

def __str__(self):
	return self.name	



   

