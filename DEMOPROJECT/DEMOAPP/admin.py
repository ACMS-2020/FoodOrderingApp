from django.contrib import admin
from .models import Order, Customer, Delivery_Person, Restaurant

# Register your models here.
admin.site.site_header = "Order Database"
admin.site.site_title = "Order"
admin.site.index_title = "Order Database"

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id','restaurant_id','user_id','items_in_order','amount','status','order_date','delivery_boy_id','delivered_date']

admin.site.register(Order,OrderAdmin)
admin.site.register(Customer)
admin.site.register(Delivery_Person)
admin.site.register(Restaurant)
