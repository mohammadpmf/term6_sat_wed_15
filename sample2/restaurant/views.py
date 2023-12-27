from django.shortcuts import render, HttpResponse

# Create your views here.
def show_welcome(request):
    return HttpResponse("Welcome to my restaurant")
def hamburger(request):
    return HttpResponse("hamburger")
def lasania(request):
    return HttpResponse("lasania")
def pizza(request):
    return HttpResponse("pizza")