from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, FoodItem, Rating, OrderUpdate, Order
from .forms import RestaurantForm, FoodItemsForm, PriceForm, AcceptableForm
from django.http import HttpResponse, HttpResponseRedirect
from .filters import ProductFilter
import json

def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants.html', {'restaurants': restaurants})

def homepage(request, id):
    restaurants = Restaurant.objects.get(id=id)
    return render(request, 'display.html', {'restaurant': restaurants})

def create_restaurant(request):
    form = RestaurantForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_restaurants')
    return render(request, 'restaurants-form.html', {'form': form})


def update_restaurant(request, id):
    restaurant = Restaurant.objects.get(id=id)
    form = RestaurantForm(request.POST or None, instance=restaurant)

    if form.is_valid():
        form.save()
        return redirect('list_restaurants')
    return render(request, 'restaurants-form.html', {'form': form, 'restaurant': restaurant})

def delete_restaurant(request, id):
    restaurant = Restaurant.objects.get(id=id)

    if request.method == 'POST':
        restaurant.delete()
        return redirect('list_restaurants')
    return render(request, 'rest-delete-confirm.html', {'restaurant': restaurant})

def add_fooditems(request):
    form = FoodItemsForm()
    if request.method == "POST":
        form = FoodItemsForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                instance = form.save(commit=false)
                #instance.restaurant = request.user
                instance.save()
                return redirect('/fooditems')
            except:
                pass
    return render(request, 'index.html', {'form': form})

def display_fooditems(request,id):
    #res = Restaurant.objects.get_object_or_404(id = id)
    food = FoodItem.objects.filter(restaurant_id=id)
    pFilter = ProductFilter(request.POST , queryset=food)
    food = pFilter.qs
    return render(request, 'foodItems.html', {'food': food, 'pFilter': pFilter })

def display(request):
    food = FoodItem.objects.all()
    pFilter = ProductFilter(request.POST, queryset = food)
    food = pFilter.qs
    return render(request, 'show.html', {'food':food, 'pFilter': pFilter})

def search(request):
    query_string = ''
    if 'q' in request.GET:
        query_string = request.GET['q']
        food = FoodItem.objects.filter(food_name__icontains = query_string)
    else:
        food = FoodItem.objects.all()
    pFilter = ProductFilter(request.POST , queryset = food)
    food = pFilter.qs
    return render(request, 'foodItems.html', {'food': food, 'pFilter': pFilter })


# @login_required
def delete_fooditems(request,id):
    try:
        food = FoodItem.objects.get(pk=id)
    except FoodItem.DoesNotExist:
        raise Http404("Food item not found ")
    food.delete()
    return redirect("/fooditems")

# @login_required
def update_price(request,id):
    food = FoodItem.objects.get(pk=id)
    form = PriceForm(instance = food)
    if request.method == "POST":
        form =PriceForm(request.POST , instance = food)
        if form.is_valid():
            try:
                form.save()
                return redirect('/fooditems')
            except:
                pass
    return render(request, 'index.html', {'form':form})


# @login_required
def update_acceptable(request,id):
    food = FoodItem.objects.get(pk=id)
    if request.method == "POST":
        form = AcceptableForm(request.POST , instance = food)
        if form.is_valid():
            try:
                form.save()
                return redirect('/fooditems')
            except:
                pass
    else:
        form = AcceptableForm(instance = food)
    return render(request, 'index.html', {'form':form})

def reviews_fooditems(request , id):
    food = FoodItem.objects.get(pk = id)
    review = Rating.objects.filter(food_id = food)
    return render(request, 'reviews.html', {'review': review})

# @login_required
def input_reviews(request , id):
    food = FoodItem.objects.get(pk = id)
    # if (Rating.objects.filter(food_id = f_id , user_id = u_id).exists()):
    #     r = Rating.objects.filter(food_id = f_id , user_id = u_id)
    #     r[reviews] = request.POST['reviews']
    #     r.save()
    # else:
    reviews = request.POST['reviews']
    r = Rating(food_id=food, reviews=reviews)
    r.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# @login_required
def input_ratings(request,id):
    food = FoodItem.objects.get(pk=id)
    # if (Rating.objects.filter(food_id = food , user_id = u_id).exists()):
    #     r = Rating.objects.filter(food_id = food , user_id = u_id)
    #     r[rating] = request.POST['rating']
    #     r.save()
    # else:
    rating = request.POST['rating']
    r = Rating( food_id=food, rating=rating)
    r.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderID', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates)
                    return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'tracker.html')



# Create your views here.

