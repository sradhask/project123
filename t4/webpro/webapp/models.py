from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class sizes(models.Models):
#     size=models.CharField()
    
class Product(models.Model):
    name=models.CharField(max_length=225)
    price=models.IntegerField()
    offerprice=models.IntegerField() 
    img=models.ImageField()
    stock=models.IntegerField()
    discription=models.TextField()
    sizes=models.CharField(max_length=225)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products_sold')


    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



    
    
     
