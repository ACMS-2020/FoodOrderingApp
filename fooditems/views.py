from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from fooditems.models import FoodItem
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
    # food = get_object_or_404(FoodItem , pk = id)
    # food.serviceable = request.POST['service']
    # food.save()
    # return HttpResponse("updated successfully")
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

# def rating(request,id,points):
#     food = get_object_or_404(FoodItem , pk = id)
#     r = food.rating
#     food.num_customers +=1
#     food.rating = (r+points) / food.num_customers
#     food.save()
#     return HttpResponse("Updated rating")
