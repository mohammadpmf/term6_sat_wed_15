from django.shortcuts import render, HttpResponse

def show_man_shop(request):
    return HttpResponse("""<img src="https://threadcurve.com/wp-content/uploads/2020/07/online-clothing-stores-for-men-july172020-min.jpg" alt="aks">""")

def show_woman_shop(request):
    return HttpResponse("ok.")

