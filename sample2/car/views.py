from django.shortcuts import render, HttpResponse

# Create your views here.
def show_welcome(request):
    return HttpResponse("Welcome to my car gallery")
def pride(request):
    return HttpResponse("""
                        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Kia_Pride_silver_vl.jpg/1200px-Kia_Pride_silver_vl.jpg" alt="a picture">
                        """)
def samand(request):
    return HttpResponse("Samand")
