from django.urls import path, include
from . import views

urlpatterns = [
    path('pride/', views.pride),
    path('pejo/', views.pejo),
    path('samand/', views.samand),
    path('reno/', views.reno),
]
