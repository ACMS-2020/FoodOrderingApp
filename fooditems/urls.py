from django.conf.urls import url
from django.urls import path
from fooditems import views

urlpatterns = [
    path('search',views.search, name = 'search'),
    path('add_fooditem', views.add_fooditems),
    path('fooditems',views.display),
    path('update_acceptable/<int:id>', views.update_acceptable),
    path('update_price/<int:id>', views.update_price),
    path('delete_fooditem/<int:id>', views.delete_fooditems),
    path('reviews_fooditem/<int:id>', views.reviews_fooditems),
    path('reviews_fooditem/input_reviews/<int:id>', views.input_reviews),
    path('display_fooditems/input_ratings/<int:id>', views.input_ratings),
    path('display_fooditems/<int:id>',views.display_fooditems),
    path('add_restaurant', views.create_restaurant, name='create_restaurants'),
    path('update_restaurant/<int:id>/', views.update_restaurant, name='update_restaurant'),
    path('delete_restaurant/<int:id>/', views.delete_restaurant, name='delete_restaurant'),
    path('', views.list_restaurants, name='list_restaurants'),
]
