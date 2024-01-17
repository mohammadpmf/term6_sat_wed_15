from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_posts, name='blog'),
    path('new/', views.new_post, name='new_post'),
    path('detail/<int:pk>/', views.show_detail, name='detail'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
