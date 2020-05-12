from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import *
from .forms import FoodItemsForm,PriceForm,AcceptableForm,RestaurantForm
from .filters import ProductFilter

# @login_required
def add_fooditems(request):
    form = FoodItemsForm()
    if request.method == "POST":
        form = FoodItemsForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                instance = form.save(commit = False)
                #instance.restaurant = request.user
                instance.save()
                return redirect('/fooditems')
            except:
                pass
    return render(request,'food_restaurant/index.html',{'form':form})

def display_fooditems(request,id):
    #res = Restaurant.objects.get_object_or_404(id = id)
    food = FoodItem.objects.filter(restaurant_id = id)
    pFilter = ProductFilter(request.POST , queryset = food)
    food = pFilter.qs
    return render(request,'food_customer/foodItems.html',{'food':food , 'pFilter' : pFilter })

def display(request):
    food = FoodItem.objects.all()
    pFilter = ProductFilter(request.POST , queryset = food)
    food = pFilter.qs
    return render(request,'food_restaurant/show.html',{'food':food , 'pFilter' : pFilter})

def search(request):
    query_string = ''
    if 'q' in request.GET:
        query_string = request.GET['q']
        food = FoodItem.objects.filter(food_name__icontains = query_string)
    else:
        food = FoodItem.objects.all()
    pFilter = ProductFilter(request.POST , queryset = food)
    food = pFilter.qs
    return render(request,'food_customer/foodItems.html',{'food':food , 'pFilter' : pFilter })


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
    return render(request,'food_restaurant/index.html',{'form':form})


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
    return render(request,'food_restaurant/index.html',{'form':form})

def reviews_fooditems(request , id):
    food = FoodItem.objects.get(pk = id)
    review = Rating.objects.filter(food_id = food)
    return render(request,'reviews.html',{'review':review})

# @login_required
def input_reviews(request , id):
    food = FoodItem.objects.get(pk = id)
    # if (Rating.objects.filter(food_id = f_id , user_id = u_id).exists()):
    #     r = Rating.objects.filter(food_id = f_id , user_id = u_id)
    #     r[reviews] = request.POST['reviews']
    #     r.save()
    # else:
    reviews = request.POST['reviews']
    r = Rating(food_id = food, reviews = reviews)
    r.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# @login_required
def input_ratings(request , id):
    food = FoodItem.objects.get(pk = id)
    # if (Rating.objects.filter(food_id = food , user_id = u_id).exists()):
    #     r = Rating.objects.filter(food_id = food , user_id = u_id)
    #     r[rating] = request.POST['rating']
    #     r.save()
    # else:
    rating = request.POST['rating']
    r = Rating( food_id = food, rating = rating)
    r.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    pFilter = ProductFilter(request.POST , queryset = restaurants)
    restaurants = pFilter.qs
    return render(request, 'restaurant_templates/restaurants.html', {'restaurants': restaurants , 'pFilter':pFilter})

def create_restaurant(request):
    form= RestaurantForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_restaurants')
    return render(request, 'restaurant_templates/restaurants-form.html', {'form': form})

# @login_required
def update_restaurant(request, id):
    restaurant = Restaurant.objects.get(id=id)
    form = RestaurantForm(request.POST or None, instance=restaurant)

    if form.is_valid():
        form.save()
        return redirect('list_restaurants')
    return render(request, 'restaurant_templates/restaurants-form.html', {'form': form, 'restaurant': restaurant})

# @login_required
def delete_restaurant(request, id):
    restaurant = Restaurant.objects.get(id=id)

    if request.method == 'POST':
        restaurant.delete()
        return redirect('list_restaurants')
    return render(request, 'restaurant_templates/rest-delete-confirm.html', {'restaurant': restaurant})
