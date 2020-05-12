from django import forms
from .models import FoodItem, Restaurant

class FoodItemsForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['food_id','food_name','restaurant_id','price','veg','item_type','cuisine_type','serviceable','image']

class PriceForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['food_id','price']

class AcceptableForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['food_id','serviceable']

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'cuisines', 'contact_no', 'avg_cost_for_a_person', 'is_delivering_now',]
