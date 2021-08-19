from django.urls import path
from ..views import product_views

urlpatterns = [
    path("", product_views.get_products, name="products"),

    path("create/", product_views.create_product, name="product-create"),
    path("<str:pk>/", product_views.get_product, name="product"),

    path("delete/<str:pk>/", product_views.delete_product, name="product-delete"),
    path("update/<str:pk>/", product_views.update_product, name="product-update"),
]
