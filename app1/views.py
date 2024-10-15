from django.shortcuts import render
from .models import Food

# Create your views here.

def home(request):
    return render(request, 'home.html')

def foods(request):
    food = Food.objects.all()
    return render(request, 'foods.html', {'foods' : food})