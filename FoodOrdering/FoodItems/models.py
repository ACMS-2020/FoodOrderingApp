from django.db import models

# Items DataBases

class FoodItem(models.Model):
	food_id = models.AutoField(primary_key=True)
	food_name = models.CharField(max_length=100)
	restaurant_id = models.IntegerField() #models.ForeignKey(Restaurant,on_delete = models.CASCADE)
	price = models.IntegerField()
	v_choice = [('veg' , 'veg'),('non-veg' , 'non-veg')]
	item_choice = [('Starters', 'Starters'), ('Main Courses', 'Main Course'), ('Desserts', 'Desserts'), ('Beverages', 'Beverages')]
	item_type = models.CharField(choices=item_choice,max_length=50 , null = True)
	s_choice = [('available', 'service available'),('not available', 'service not available')]
	serviceable = models.CharField(max_length=30, choices=s_choice, default='service available')
	veg = models.CharField(max_length=100 , choices=v_choice, default='veg')
	cuisine_type = models.CharField(max_length=100)
	image = models.ImageField(upload_to='gallery/',blank=True,null=True)

	def no_of_ratings(self):
		r = Rating.objects.filter(food_id = self).count()
		return r

	def avg_rating(self):
		sum=0
		ratings = Rating.objects.filter(food_id = self)
		for r in ratings:
			sum+=r.rating
		if (len(ratings)>0):
			return round(sum/len(ratings),1)
		return 0


class Rating(models.Model):
	food_id = models.ForeignKey(FoodItem,on_delete = models.CASCADE)
	user_id = models.CharField(max_length=100 , default =1)
	rating = models.IntegerField(default = 0, null = True)
	reviews = models.TextField(max_length = 400 , null = True)


#Restaurant Databses

class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    cuisines = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    avg_cost_for_a_person = models.IntegerField()
    is_delivering_now = models.BooleanField(default=True)
    restaurant_image = models.ImageField()
    #rating = models.DecimalField(max_digits=2, decimal_places=1,null=True)
