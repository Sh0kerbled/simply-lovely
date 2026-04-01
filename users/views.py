from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm

def auth_page(request):
    context = {'form': UserLoginForm()}
    return render(request, 'auth.html', context)

def join_page(request):
    return render(request, 'register.html')