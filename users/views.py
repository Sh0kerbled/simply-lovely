from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm

def auth_page(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            password = form.cleaned_data['password']
            user = authenticate(full_name=full_name, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

    return render(request, 'auth.html', {'form': form})

def join_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})