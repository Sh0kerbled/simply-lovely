from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def auth_page(request):
    return render(request, 'auth.html')

def join_page(request):
    return render(request, 'register.html')