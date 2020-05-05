from django.conf.urls import url
from django.urls import path
from .views import list_restaurants, create_restaurant, update_restaurant, delete_restaurant

urlpatterns = [
    path('', list_restaurants, name='list_restaurants'),
    path('new', create_restaurant, name='create_restaurants'),
    path('update/<int:id>/', update_restaurant, name='update_restaurant'),
    path('delete/<int:id>/', delete_restaurant, name='delete_restaurant'),
]

