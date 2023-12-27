from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_posts, name='blog'),
    path('detail/<int:pk>/', views.show_detail, name='detail'),
]
