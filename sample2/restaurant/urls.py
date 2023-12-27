from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_welcome, name='restaurant_welcome'),
    path('pizza/', views.pizza, name='pizza'),
    path('hamburger/', views.hamburger, name='hamburger'),
    path('lasania/', views.lasania, name='lasania'),
]
