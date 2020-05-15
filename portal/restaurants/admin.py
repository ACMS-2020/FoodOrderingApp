from django.contrib import admin
from .models import *
class OrderInline(admin.TabularInline):
    model = Rating
    extra=0


class FIAdmin(admin.ModelAdmin):
	list_display = ['food_name','restaurant_id','price','veg','item_type','cuisine_type','serviceable','image']
	inlines = [OrderInline]

admin.site.register(FoodItem,FIAdmin)
admin.site.register(Restaurant)
admin.site.register(OrderUpdate)
admin.site.register(Order)


# Register your models here.

