from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .models import *
from datetime import datetime
current_user = "kou"
# Create your views here.
def display_items(request,res_id):
    items = FoodItem.objects.filter(restaurant_id=res_id)
    context = {'items':items}
    return render(request,'items.html',context)

def addToCart(request,item_id):
    try:
        cartTrail = Cart.objects.get(food_id=item_id)
        cartTrail.quantity += 1
        cartTrail.save()
    except Cart.DoesNotExist:
        items = FoodItem.objects.filter(food_id=item_id)[0]
        cartItem = Cart.objects.create(user_id=current_user, res_id=items.restaurant_id, food_id=item_id)
        cartItem.save()

    return HttpResponse("Added")

def checkOut(request):
    cart = Cart.objects.filter(user_id=current_user)
    if(not cart.exists()):
        return HttpResponse('No items in cart')
    order = Order.objects.create(user_id=current_user,restaurant_id=cart[0].res_id)
    for i in cart:
        order.order_set.create(item_id=i.food_id,quantity=i.quantity)
        item = FoodItem.objects.filter(food_id=i.food_id)
        order.amount += i.quantity*item[0].price
    order.save()
    cart.delete()
    return HttpResponse("Order placed")

def res_pending_order(request, res_id):
    obj = Order.objects.filter(restaurant_id=res_id,status="Placed")
    paginator = Paginator(obj, 2)
    page = request.GET.get('page')
    values = paginator.get_page(page)
    context = {'obj':obj,'rest_id':res_id,'values':values}
    return render(request,'order_pending.html',context)

def res_processing_order(request,res_id):
    obj = Order.objects.filter(restaurant_id=res_id,status="Processing")
    page = request.GET.get('page')
    paginator = Paginator(obj, 5)
    try:
        values = paginator.page(page)
    except PageNotAnInteger:
        values = paginator.page(1)
    except EmptyPage:
        values = paginator.page(paginator.num_pages)
    context = {'obj':obj,'rest_id':res_id,'values':values}
    return render(request,'order_processed.html',context)

def res_dispatched_order(request,res_id):
    obj = Order.objects.filter(restaurant_id=res_id,status="In Delivery")
    page = request.GET.get('page', 1)
    paginator = Paginator(obj, 5)
    try:
        values = paginator.page(page)
    except PageNotAnInteger:
        values = paginator.page(1)
    except EmptyPage:
        values = paginator.page(paginator.num_pages)
    context = {'obj':obj,'rest_id':res_id,'values':values}
    return render(request,'order_dispatched.html',context)

def accept_order(request,order_id):
    obj = Order.objects.get(order_id=order_id)
    obj.order_accepted()
    obj.save()
    return redirect('/food/res_pending_order/'+obj.restaurant_id)

def processed_order(request,order_id):
    obj = Order.objects.get(order_id=order_id)
    obj.order_processed()
    obj.save()
    return redirect('/food/res_processing_order/'+obj.restaurant_id)