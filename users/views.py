from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm, UserEditForm, SalerRegistrationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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

@login_required
def profile_page(request):
    return render(request, 'profile.html')

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserEditForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile_page'))
        else:
            print(form.errors)
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'profile_edit.html', {'form': form})

def saler_register(request):
    if request.method == 'POST':
        form = SalerRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:auth_page'))
    else:
        form = SalerRegistrationForm()
    return render(request, 'saler_register.html', {'form': form})