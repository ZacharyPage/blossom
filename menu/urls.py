from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('food/<int:food_id>/', views.detail_food, name='detail_food'),
    path('beverage/<int:beverage_id>/', views.detail_beverage, name='detail_beverage'),
]
