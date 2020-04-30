from django.contrib import admin
from .models import FoodItem

# Register your models here.
class FIAdmin(admin.ModelAdmin):
	list_display = ['food_name','restaurant_id','price','veg','cuisine_type','serviceable','image']

admin.site.register(FoodItem,FIAdmin)
