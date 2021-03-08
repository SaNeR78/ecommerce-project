from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def detailed_product(request):
    return render(request, 'detailed_product.html')

