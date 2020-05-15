from django.conf.urls import url
from django.urls import path
from .views import list_restaurants, create_restaurant, update_restaurant, delete_restaurant, homepage, search, add_fooditems, display, update_acceptable, update_price, delete_fooditems, reviews_fooditems, input_reviews, input_ratings, display_fooditems, tracker
urlpatterns = [
    path('', list_restaurants, name='list_restaurants'),
    path('new', create_restaurant, name='create_restaurants'),
    path('update/<int:id>/', update_restaurant, name='update_restaurant'),
    path('delete/<int:id>/', delete_restaurant, name='delete_restaurant'),
    path('home/<int:id>/', homepage, name='homepage'),
    path('search', search, name='search'),
    path('add_fooditem', add_fooditems, name='add_fooditems'),
    path('fooditems', display, name='display'),
    path('update_acceptable/<int:id>/', update_acceptable, name='update_acceptable'),
    path('update_price/<int:id>/', update_price, name='update_price'),
    path('delete_fooditem/<int:id>/', delete_fooditems, name='delete_fooditems'),
    path('reviews_fooditem/<int:id>/', reviews_fooditems, name='reviews_fooditems'),
    path('reviews_fooditem/input_reviews/<int:id>/', input_reviews, name='input_reviews'),
    path('display_fooditems/input_ratings/<int:id>/', input_ratings, name='input_ratings'),
    path('display_fooditems/<int:id>/', display_fooditems, name='display_fooditems'),
    path('tracker', tracker, name='tracker')

]


