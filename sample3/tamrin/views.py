from django.shortcuts import render

def tamrin1(request):
    context = {
        'name': 'Reza',
        'surname': 'Ahmadi',
        'phone_number': '09112541148',
    }
    return render(request, 'car/tamrin1.html', context)

def tamrin2(request):
    return render(request, 'sportcar/tamrin2.html')
