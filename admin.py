from django.contrib import admin

# Register your models here.

from .models import Customer, Delivery_Person, Restaurant

admin.site.register(Customer)
admin.site.register(Delivery_Person)
admin.site.register(Restaurant)
