from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm

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


# Create your views here.
