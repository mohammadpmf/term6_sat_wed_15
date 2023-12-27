from django.shortcuts import render
from . import models

def show_tamrin(request):
    context = {'games': models.Game.objects.all()}
    return render(request, 'index.html', context)