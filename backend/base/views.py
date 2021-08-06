from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def get_routes(request):
    routes = [
        "/api/products",
        "/api/products/create/",

        "/api/products/upload",

        "/api/products/<id>/reviews/",

        "/api/products/top/",
        "/api/products/<id>/",

        "/api/products/delete/<id>/",
        "/api/products/<upload>/<id>/"
    ]
    return JsonResponse(routes, safe=False)
