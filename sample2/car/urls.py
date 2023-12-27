from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_welcome, name='car_welcome'),
    path('pride/', views.pride, name='pride'),
    path('samand/', views.samand, name='samand'),
]
