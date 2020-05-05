from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'cuisines', 'contact_no', 'avg_cost_for_a_person', 'is_delivering_now', 'rating']