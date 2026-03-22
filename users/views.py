from django.shortcuts import render

def auth_page(request):
    return render(request, 'auth.html')

def join_page(request):
    return render(request, 'register.html')