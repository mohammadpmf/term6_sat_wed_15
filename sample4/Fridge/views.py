from django.shortcuts import render
from . import models

def show_all_fridges(request):
    context = {
        'name': 'ali',
        'age': 40,
        'fridges': models.Fridge.objects.all()
    }
    return render (request, 'yakhchal.html', context)