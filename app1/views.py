from django.shortcuts import render, redirect
from .models import Food, Category
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

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

@login_required
def cart(request):
    return render(request, 'cart.html')

@login_required
def add_to_cart(request):
    pass

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form' : form})