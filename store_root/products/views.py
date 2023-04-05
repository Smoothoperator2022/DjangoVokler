from django.shortcuts import render
# functions = controllers = views
# Create your views here.
from products.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'Store', # variables (placeholders)
        'is_promotion' : True # template tags
               }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'category': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)