from django.db import models

# Create your models here.

class category(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    slue = models.CharField(max_length=100)
    date = models.DateField()
    slue = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class subcategory(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    slue = models.CharField(max_length=100)
    category = models.ForeignKey(category, on_delete=models.CASCADE , related_name='category')

    def __str__(self):
        return self.title
    
class Product(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    price = models.DateField()
    slue = models.CharField(max_length=100)
    subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE , related_name='subcategory')

    def __str__(self):
        return self.title
    
