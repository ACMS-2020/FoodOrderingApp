from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from fooditems.models import FoodItem,Rating
from fooditems.forms import FoodItemsForm,PriceForm,AcceptableForm

def food(request):
    form = FoodItemsForm()
    if request.method == "POST":
        form = FoodItemsForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    return render(request,'index.html',{'form':form})

def display(request):
    food = FoodItem.objects.all()
    return render(request,'show.html',{'food':food})

def delete(request,id):
    try:
        food = FoodItem.objects.get(pk=id)
    except FoodItem.DoesNotExist:
        raise Http404("Food item not found ")
    food.delete()
    return redirect("/")

def update_price(request,id):
    food = FoodItem.objects.get(pk=id)
    form = PriceForm(instance = food)
    if request.method == "POST":
        form =PriceForm(request.POST , instance = food)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    return render(request,'index.html',{'form':form})

def update_acceptable(request,id):
    food = FoodItem.objects.get(pk=id)
    if request.method == "POST":
        form = AcceptableForm(request.POST , instance = food)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = AcceptableForm(instance = food)
    return render(request,'index.html',{'form':form})

def rating(request,id):
    food = FoodItem.Objects.get(pk = id)
    return render(request,'show.html',{'food':food})

def reviews(request , id):
    review = Rating.objects.filter(food_id = id)
    return render(request,'reviews.html',{'review':review})

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
