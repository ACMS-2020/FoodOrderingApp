from django.db import models

class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    address = models.CharField(max_length=500)
    cuisines = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    avg_cost_for_a_person = models.IntegerField()
    is_delivering_now = models.BooleanField(default=True)
    #rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name

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
	food_id = models.ForeignKey(FoodItem, on_delete = models.CASCADE)
	user_id = models.CharField(max_length=100, default =1)
	rating = models.IntegerField(default=0, null=True)
	reviews = models.TextField(max_length=400, null=True)

class Order(models.Model):
	order_id = models.AutoField(primary_key=True)
	email = models.CharField(max_length=200)
	restaurant_id = models.CharField(max_length=200)
	user_id = models.CharField(max_length=200)
	amount = models.FloatField(default=0)
	status_choices = [("Rejected","Rejected"),("Order Picked","Order Picked"),("Delivery Boy Assigned","Delivery Boy Assigned"),("Placed","Placed"),("Processing","Processing"),("In Delivery","In Delivery"),("Delivered","Delivered"),("Cancelled","Cancelled")]
	status = models.CharField(choices=status_choices,max_length=500,default="Placed")
	order_date = models.DateTimeField(auto_now_add=True)
	delivery_boy_id = models.CharField(max_length=200,default="not_assigned")
	delivered_date = models.DateTimeField(blank=True, null=True)

class OrderUpdate(models.Model):
	update_id = models.AutoField(primary_key=True)
	order_id = models.IntegerField(default="")
	update_desc=models.CharField(max_length=5000)
	timestamp = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.update_desc[0:7] + "..."











# Create your models here.

