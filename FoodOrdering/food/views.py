from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .models import *
from datetime import datetime
current_user = "Susmitha"
items_per_page = 4
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
        cartItem = Cart.objects.create(user_id=current_user, res_id=items.restaurant_id, food_id=item_id,food_name=items.food_name,price=items.price)
        cartItem.save()

    return HttpResponse("Added")

def removeFromCart(request,item_id):
    cartTrail = Cart.objects.get(food_id=item_id)
    cartTrail.delete()
    return redirect('/food/cart')

def checkOut(request):
    cart = Cart.objects.filter(user_id=current_user)
    if(not cart.exists()):
        return HttpResponse('No items in cart')
    order = Order.objects.create(user_id=current_user,restaurant_id=cart[0].res_id)
    for i in cart:
        order.order_set.create(item_id=i.food_id,quantity=i.quantity,item_name=i.food_name)
        item = FoodItem.objects.filter(food_id=i.food_id)
        order.amount += i.quantity*item[0].price
    order.save()
    cart.delete()
    return HttpResponse("Order placed")

def res_pending_order(request, res_id):
    obj = Order.objects.filter(restaurant_id=res_id,status="Placed")
    paginator = Paginator(obj,items_per_page)
    page = request.GET.get('page')
    if page==None:
        page = 1
    ind = int(page)-1
    obj = obj[ind*items_per_page:ind*items_per_page+items_per_page]
    values = paginator.get_page(page)
    context = {'obj':obj,'rest_id':res_id,'values':values}
    return render(request,'order_pending.html',context)

def res_processing_order(request,res_id):
    obj = Order.objects.filter(restaurant_id=res_id,status="Processing").order_by("-order_id")
    paginator = Paginator(obj,items_per_page)
    page = request.GET.get('page')
    if page==None:
        page = 1
    ind = int(page)-1
    obj = obj[ind*items_per_page:ind*items_per_page+items_per_page]
    values = paginator.get_page(page)
    context = {'obj':obj,'rest_id':res_id,'values':values}
    return render(request,'order_processed.html',context)

def res_dispatched_order(request,res_id):
    obj = Order.objects.filter(restaurant_id=res_id,status="In Delivery")
    paginator = Paginator(obj,items_per_page)
    page = request.GET.get('page')
    if page==None:
        page = 1
    ind = int(page)-1
    obj = obj[ind*items_per_page:ind*items_per_page+items_per_page]
    values = paginator.get_page(page)
    context = {'obj':obj,'rest_id':res_id,'values':values}
    return render(request,'order_dispatched.html',context)

def accept_order(request,order_id):
    obj = Order.objects.get(order_id=order_id)
    obj.order_accepted()
    obj.save()
    return redirect('/food/res_pending_order/'+obj.restaurant_id)

def reject_order(request,order_id):
    obj = Order.objects.get(order_id=order_id)
    obj.order_rejected()
    return redirect('/food/res_pending_order/'+obj.restaurant_id)

def processed_order(request,order_id):
    obj = Order.objects.get(order_id=order_id)
    obj.order_processed()
    obj.save()
    return redirect('/food/res_processing_order/'+obj.restaurant_id)

def user_order_details(request):
    obj = Order.objects.filter(user_id=current_user).order_by('-order_id')
    paginator = Paginator(obj, items_per_page)
    page = request.GET.get('page')
    if page == None:
        page = 1
    ind = int(page) - 1
    obj = obj[ind * items_per_page:ind * items_per_page + items_per_page]
    values = paginator.get_page(page)
    return render(request,'user_orders.html',{'obj':obj,'values':values})


def reorder(request,order_id):
    obj = Order.objects.get(order_id=order_id)
    re_obj = Order.objects.create(user_id=obj.user_id,restaurant_id=obj.restaurant_id)
    items = obj.order_set.all()
    current_amount =0
    for i in items:
        print("In for",current_amount)
        re_obj.order_set.create(item_id=i.item_id,quantity=i.quantity)
        foo = FoodItem.objects.get(food_id=i.item_id)
        if foo:
            current_amount +=  foo.price*i.quantity
    re_obj.amount = current_amount
    re_obj.save()
    return HttpResponse("reordered")

def orders_available(request):
    obj = Order.objects.filter(status="In Delivery")
    paginator = Paginator(obj, items_per_page)
    page = request.GET.get('page')
    if page == None:
        page = 1
    ind = int(page) - 1
    obj = obj[ind * items_per_page:ind * items_per_page + items_per_page]
    values = paginator.get_page(page)
    return render(request, 'delivery_available.html', {'obj': obj, 'values': values,'delivery_boy_id':current_user})

def your_delivery(request):
    obj = Order.objects.filter(delivery_boy_id=current_user).order_by('-order_date')
    paginator = Paginator(obj, items_per_page)
    page = request.GET.get('page')
    if page == None:
        page = 1
    ind = int(page) - 1
    obj = obj[ind * items_per_page:ind * items_per_page + items_per_page]
    values = paginator.get_page(page)
    return render(request, 'your_delivery.html', {'obj': obj, 'values': values})


def accept_delivery(request,order_id):
    obj = Order.objects.get(order_id=order_id)
    obj.delivery_accepted()
    obj.delivery_boy_id=current_user
    obj.save()
    return redirect('/food/orders_available/')

def order_picked(request,order_id):
    obj = Order.objects.get(order_id=order_id)
    obj.delivery_picked()
    obj.save()
    return redirect('/food/your_delivery/')

def order_delivered(request,order_id):
    obj = Order.objects.get(order_id=order_id)
    obj.order_delivered()
    obj.save()
    return redirect('/food/your_delivery/')


def cart(request):
    obj =  Cart.objects.filter(user_id=current_user)
    return render(request,"cart.html",{'cart_items':obj})


