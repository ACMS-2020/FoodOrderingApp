from django.db import models

# Create your models here.

class FoodItem(models.Model):
	food_id = models.AutoField(primary_key=True)
	food_name = models.CharField(max_length=100)
	restaurant_id = models.CharField(max_length=100)
	#models.ForeignKey(restaurants,on_delete = models.CASCADE)
	price = models.IntegerField()
	veg = models.BooleanField(default=True)
	cuisine_type = models.CharField(max_length=100)
	serviceable = models.BooleanField(default=True)
	rating = models.DecimalField(max_digits=2 , decimal_places=1,default=0.0)
	#num_customers = models.IntegerField(default=0)
	image = models.ImageField(upload_to='gallery/',blank=True,null=True)

#class Rating(models.Model):
