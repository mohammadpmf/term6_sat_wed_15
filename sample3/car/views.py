from django.shortcuts import render

def pride(request):
    return render(request, 'pride.html')

def pejo(request):
    return render(request, 'pejo.html')

def samand(request):
    return render(request, 'samand.html')

def reno(request):
    return render(request, 'reno.html')
