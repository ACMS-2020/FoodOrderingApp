from django.conf.urls import url
from django.urls import path
from . import views
from . views import *

app_name = "food"

urlpatterns=[
    url(r'^items/(?P<res_id>\d+)/$',views.display_items,name="items"),
    url(r'^addToCart/(?P<item_id>\d+)/$',views.addToCart,name="addToCart"),
    url('checkOut/',views.checkOut,name="checkOut"),
    url('res_pending_order/(?P<res_id>\d+)/$',views.res_pending_order,name="res_pending_order"),
    url('res_processing_order/(?P<res_id>\d+)/$',views.res_processing_order,name="res_processing_order"),
    url('res_dispatched_order/(?P<res_id>\d+)/$',views.res_dispatched_order,name="res_dispatched_order"),
    url('accept_order/(?P<order_id>\d+)/$',views.accept_order,name="accept_order"),
    url('processed_order/(?P<order_id>\d+)/$',views.processed_order,name="processed_order"),
]