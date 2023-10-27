from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Category") 
    
    
class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name  

    class Meta:
        verbose_name = ("Subcategory")
        verbose_name_plural = ("Subcategory") 


class Product(models.Model):
    subcategory = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    image = models.ImageField()
    images = models.ImageField()
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Product") 