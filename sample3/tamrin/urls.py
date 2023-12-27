from django.urls import path, include
from . import views

urlpatterns = [
    path('tamrin1/', views.tamrin1),
    path('tamrin2/', views.tamrin2),
]
