from django.db import models
from datetime import datetime

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    restaurant_id = models.CharField(max_length=200)    #foreign_key
    user_id = models.CharField(max_length=200)          #foreign_key
    items_in_order = models.CharField(max_length=500) #Todo
    amount = models.FloatField()
    status_choices = [("Placed","Placed"),("Processing","Processing"),("In Delivery","In Delivery"),("Delivered","Delivered"),("Cancelled","Cancelled")]
    status = models.CharField(choices=status_choices,max_length=500,default="Placed")
    order_date = models.DateTimeField(default=datetime.now())
    delivery_boy_id = models.CharField(max_length=200,default="not_assigned")
    delivered_date = models.DateTimeField(blank=True, null=True)

    # for items"_in_order : Carrot:20,Potato:30"

    def get_order_items(self):
        items_array = self.items_in_order.split(',')
        items = {}
        for i in items_array:
            name,price = i.split(":")
            items.append({name,price})
        return items

    def order_accepted(self):
        if(self.status=="Placed"):
            self.status = "Processing"
            self.save()
            return True
        else:
            print("Invalid operation")
            return False

    def order_processed(self):
        if(self.status=="Processing"):
            self.status = "In Delivery"
            self.save()
            return True
        else:
            print("Invalid operation")
            return False

    def order_delivered(self):
        if(self.status=="In Delivery"):
            self.status = "Delivered"
            self.delivered_date=datetime.now()
            self.save()
            return True
        else:
            print("Invalid operation")
            return False

    def cancel_order(self):
        if(self.status=="Placed"):
            self.status="Cancelled"
            self.save()
            return True
        else:
            print("Invalid operation")
            return False

    def __str__(self):
        return "Your order id is dont no"