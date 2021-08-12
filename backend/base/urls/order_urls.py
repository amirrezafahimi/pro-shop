from django.urls import path
from ..views import order_views

urlpatterns = [
    path("add/", order_views.add_order_items, name="orders-add"),
]
