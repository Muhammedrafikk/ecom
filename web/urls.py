from django.contrib import admin
from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    
    path('', views.shop_search_results,name="shop_search_results")

]