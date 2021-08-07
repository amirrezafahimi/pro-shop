from django.http import JsonResponse
# from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializer import ProductSerializer


# Create your views here.
@api_view(["GET"])
def get_routes(request):
    routes = [
        "/api/products.py",
        "/api/products.py/create/",

        "/api/products.py/upload",

        "/api/products.py/<id>/reviews/",

        "/api/products.py/top/",
        "/api/products.py/<id>/",

        "/api/products.py/delete/<id>/",
        "/api/products.py/<upload>/<id>/"
    ]
    return Response(routes)


@api_view(["GET"])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_product(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
