from django.contrib import admin
from.models import Product
from.models import category,subcategory

# Register your models here.


@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('title','date','slue')
    list_filter = ("title", "date",'slue' )
    search_fields = ("title","date",'slue')
    prepopulated_fields = {'slue': ('title',)}

@admin.register(subcategory)
class subcategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slue')
    list_filter = ("title",'slue' )
    search_fields = ("title",'slue')
    prepopulated_fields = {'slue': ('title',)}


@admin.register(Product)
class subcategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slue')
    list_filter = ("title",'slue' )
    search_fields = ("title",'slue')
    prepopulated_fields = {'slue': ('title',)}






