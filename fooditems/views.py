from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from fooditems.models import FoodItem,Rating,Restaurant
from fooditems.forms import FoodItemsForm,PriceForm,AcceptableForm,RestaurantForm

def add_fooditems(request):
    form = FoodItemsForm()
    if request.method == "POST":
        form = FoodItemsForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('food_restaurant/display_fooditems')
            except:
                pass
    return render(request,'food_restaurant/index.html',{'form':form})

def display_fooditems(request,id):
    food = FoodItem.objects.filter(restaurant_id = id)
    return render(request,'food_customer/foodItems.html',{'food':food})

def display(request):
    food = FoodItem.objects.all()
    return render(request,'food_restaurant/show.html',{'food':food})

def delete_fooditems(request,id):
    try:
        food = FoodItem.objects.get(pk=id)
    except FoodItem.DoesNotExist:
        raise Http404("Food item not found ")
    food.delete()
    return redirect("food_restaurant/display_fooditems")

def update_price(request,id):
    food = FoodItem.objects.get(pk=id)
    form = PriceForm(instance = food)
    if request.method == "POST":
        form =PriceForm(request.POST , instance = food)
        if form.is_valid():
            try:
                form.save()
                return redirect('food_restaurant/display_fooditems')
            except:
                pass
    return render(request,'food_restaurant/index.html',{'form':form})

def update_acceptable(request,id):
    food = FoodItem.objects.get(pk=id)
    if request.method == "POST":
        form = AcceptableForm(request.POST , instance = food)
        if form.is_valid():
            try:
                form.save()
                return redirect('food_restaurant/display_fooditems')
            except:
                pass
    else:
        form = AcceptableForm(instance = food)
    return render(request,'food_restaurant/index.html',{'form':form})

def reviews_fooditems(request , id):
    review = Rating.objects.filter(food_id = id)
    return render(request,'reviews.html',{'review':review})

# @login_required
# def input_reviews(request , f_id , u_id):
#     if (Rating.objects.filter(food_id = f_id , user_id = u_id).exists()):
#         r = Rating.objects.filter(food_id = f_id , user_id = u_id)
#         r[reviews] = request.POST['reviews']
#         r.save()
#     else:
#         reviews = request.POST['reviews']
#         r = Rating(user_id = u_id , food_id = f_id, reviews = reviews)
#         r.save()
#     return render(request,'reviews.html',{'review':r})


# @login_required
# def input_ratings(request , f_id , u_id):
#     if (Rating.objects.filter(food_id = f_id , user_id = u_id).exists()):
#         r = Rating.objects.filter(food_id = f_id , user_id = u_id)
#         r[rating] = request.POST['rating']
#         r.save()
#     else:
#         rating = request.POST['rating']
#         r = Rating(user_id = u_id , food_id = f_id, rating = rating)
#         r.save()
#     food = FoodItem.Objects.get(pk = f_id)
#     return render(request,'show.html',{'food':food})


def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants.html', {'restaurants': restaurants})

def create_restaurant(request):
    form= RestaurantForm(request.POST or None)

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
