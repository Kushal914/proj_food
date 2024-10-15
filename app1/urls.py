from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('categories/', views.categories, name='categories'),
    path('foods/', views.foods, name = 'foods'),
    path('category-foods/<int:category_id>/', views.category_foods, name='category_foods'),
]