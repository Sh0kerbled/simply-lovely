from django.shortcuts import render, redirect, HttpResponseRedirect, messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def auth_page(request):
    return render(request, 'auth.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect("/dashboard/")