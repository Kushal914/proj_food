from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=31)
    photo = models.ImageField(upload_to='images/categories/', blank=False, null=False)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'
    
class Food(models.Model):
    title = models.CharField(max_length=31)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Added price attribute
    photo = models.ImageField(upload_to='images/foods/', blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Added category attribute
    is_veg = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'
    
class Cart(models.Model):
    PAY_MODE_CHOICES = [
        ('CoD', 'Cash on Delivery'),
    ]

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_mode = models.CharField(max_length=15, choices=PAY_MODE_CHOICES, default='CoD')
    status = models.CharField(max_length=31, default='ordered')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    food = models.ForeignKey(Food, on_delete = models.CASCADE)
    qty = models.IntegerField(default=0)