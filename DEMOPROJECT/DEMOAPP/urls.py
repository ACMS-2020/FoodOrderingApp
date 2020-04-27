from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('place_order/',views.place_order,name="order page"),
    url(r'^delete_order/(?P<orders_id>\d+)/$',views.delete_order,name="delete_order"),
    url(r'^delivered/(?P<orders_id>\d+)/$',views.delivered,name="order_delivered"),
    url(r'^accept/(?P<orders_id>\d+)/$',views.accept_order,name="accept_order"),
    url(r'^delivering/(?P<orders_id>\d+)/$',views.delivering_order,name="order_delivering"),
    url(r'^my_orders/(?P<users_id>\d+)/$',views.display_orders,name="my_orders"),
    url(r'^my_res_orders/(?P<orders_id>\d+)/$',views.res_orders,name="my_orders")
]