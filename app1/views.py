from django.shortcuts import render
from .models import Food, Category

# Create your views here.

def home(request):
    category_items = Category.objects.filter(is_active=True, is_featured=True)
    food_items = Food.objects.filter(is_active=True, is_featured=True)
    return render(request, 'home.html', {'category_items': category_items, 'food_items' : food_items})

def categories(request):
    category_items = Category.objects.filter(is_active=True)
    return render(request, 'categories.html', {'category_items': category_items})

def foods(request):
    food_items = Food.objects.filter(is_active=True)
    return render(request, 'foods.html', {'food_items' : food_items})

def category_foods(request, category_id):
    food_items = Food.objects.filter(category__id=category_id, is_active=True)
    return render(request, 'foods.html', {'food_items' : food_items})