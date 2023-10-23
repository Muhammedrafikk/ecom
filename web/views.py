from django.shortcuts import render
from django.views.generic import ListView
from . models import category,subcategory
from . models import Product

# Create your views here.

class index(ListView):
    model = Product
    template_name = "web/index.html"
    context_object_name = 'product'

class category(ListView):
    model = category
    template_name = "web/category.html"
    context_object_name = 'category'

class subcategory(ListView):
    model = subcategory
    template_name = "web/subcategory.html"
    context_object_name = 'subcategory'

def index_2(request):
    return render(request, 'web/index_2.html')

def shop_search_results(request):

    return render(request, "web/shop_search_results.html")
    









