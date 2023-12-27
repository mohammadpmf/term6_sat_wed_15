from django.urls import path
from . import views

urlpatterns = [
    path('man/', views.show_man_shop, name='man'),
    path('woman/', views.show_woman_shop, name='woman'),
]
