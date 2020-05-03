from django import forms
from fooditems.models import FoodItem

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
