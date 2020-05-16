from django.conf.urls import url
from django.urls import path
from . import views

app_name="FoodItems"

urlpatterns = [
    path('restaurant_fooditems',views.display),
    path('res_search',views.res_search, name = 'res_search'),
    path('display_fooditems/<str:username>',views.display_fooditems , name='display_fooditems'),
    path('display_fooditems/search/<str:username>',views.search, name = 'search'),
    path('add_fooditem', views.add_fooditems),
    path('update_acceptable/<int:id>', views.update_acceptable),
    path('update_price/<int:id>', views.update_price),
    path('delete_fooditem/<int:id>', views.delete_fooditems),
    # path('reviews_fooditem/<int:id>', views.reviews_fooditems),
    path('input_reviews/<int:id>', views.input_reviews),
    path('input_ratings/<int:id>', views.input_ratings),
    # path('add_restaurant', views.create_restaurant, name='create_restaurants'),
    path('update_restaurant/<str:username>/', views.update_restaurant, name='update_restaurant'),
    path('delete_restaurant/<str:username>/', views.delete_restaurant, name='delete_restaurant'),
    path('', views.list_restaurants, name='list_restaurants'),
]
