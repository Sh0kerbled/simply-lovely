from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import logout

def auth_page(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'auth.html', context)

def join_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:auth_page'))
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def profile_page(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def reset_password_page(request):
    return render(request, 'account_reset_form.html')