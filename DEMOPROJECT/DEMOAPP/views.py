from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
from random import  randint
from datetime import datetime
# Create your views here.

'''
Operations that a user can perform are
1.Place new order
2.Delete a placed order before it is accepted by the restaurant
'''

def place_order(request):
    obj = Order(
        restaurant_id=request.POST["restaurant_id"],user_id=request.POST["user_id"],
        items_in_order=request.POST["items"],amount=request.POST["amount"],order_date=datetime.now()
    )
    obj.save()
    return HttpResponse("Order Placed id: "+obj.order_id)

def delete_order(request,orders_id):
    print(orders_id)
    obj= Order.objects.get(order_id=orders_id)
    if obj.cancel_order():
        return HttpResponse("Order Cancelled")
    return HttpResponse("Order cannot be cancelled")

def display_orders(request,users_id):
    obj = Order.objects.filter(user_id=users_id)
    context = {'obj':obj}
    return render(request,'DEMOAPP/display_order.html',context)


'''
Operations that can be performed by a deliver personnel
1.Update the status of the order to delivered after delivery
'''

def delivered(request,orders_id):
    obj=Order.objects.get(order_id=orders_id)
    if obj.order_delivered():
        return HttpResponse("Order delivered at your door step")
    return HttpResponse("Problem with delivery boy")

'''
Operations that a restaurant can perform
1.Accept the order
2.deliver the order
'''

def accept_order(request,orders_id):
    obj=Order.objects.get(order_id=orders_id)
    if obj.order_accepted():
        return HttpResponse("Order is accepted and is being processed")
    return HttpResponse("Order cannot be accepted")

def delivering_order(request,orders_id):
    obj=Order.objects.get(order_id=orders_id)
    if obj.order_processed():
        return HttpResponse("Order in delivering")
    return HttpResponse("error in deliverying")

def res_orders(request,res_id):
    obj = Order.objects.get(restaurant_id = res_id).order_by('-order_date')
    context = {'obj':obj}
    return render(request,'DEMOAPP/display_order.html',context)




