from django.urls import path
from ..views import order_views

urlpatterns = [
    path("", order_views.get_orders, name="orders"),
    path("add/", order_views.add_order_items, name="orders-add"),
    path("myorders/", order_views.get_my_orders, name="myorders"),

    path("<str:pk>/", order_views.get_order_by_id, name="user-order"),
    path("<str:pk>/pay/", order_views.update_order_to_paid, name="pay"),
]
