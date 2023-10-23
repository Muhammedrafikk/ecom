from django.contrib import admin
from django.urls import path
from . import views

app_name = "web"

urlpatterns = [

    path('', views.index.as_view(),name="index"),
    path("shop_search_results/", views.shop_search_results, name="shop_search_results"), 
    path('category/', views.category.as_view(),name="category"),
    path('subcategory/', views.subcategory.as_view(),name="subcategory"),
    path("index_2/", views.index_2, name="index_2"), 

]