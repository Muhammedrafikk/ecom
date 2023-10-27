from django.shortcuts import render
# from django.views.generic import ListView

from . models import Category,Product

# Create your views here.

def shop_search_results(request):

    category = Category.objects.all()
    
    categoryID = request.GET.get('category')

    if categoryID :
        product = Product.objects.filter(subcategory = categoryID)

    else :
        product = Product.objects.all()

    context = {
        'category' : category,
        'prod' : product,
    }
    return render(request , "web/shop_search_results.html" , context)
