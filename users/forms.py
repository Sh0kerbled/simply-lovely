from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from users.models import CustomUser

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'block w-full rounded-lg border border-gray-300 py-3 pl-10 pr-4 placeholder-gray-400 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900/50 sm:text-sm transition-all', 'placeholder': 'Pimpy'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'block w-full rounded-lg border border-gray-300 py-3 pl-10 pr-4 placeholder-gray-400 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900/50 sm:text-sm transition-all', 'placeholder': '••••••••'}))
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    error_messages = {
        'invalid_login': "Your custom 'incorrect username or password' message here.",
    }
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'block w-full rounded-lg border border-gray-300 py-3 pl-10 pr-4 placeholder-gray-400 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900/50 sm:text-sm transition-all', 'placeholder': 'Pimpy'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'class="block w-full rounded-lg border border-gray-300 py-3 pl-10 pr-4 placeholder-gray-400 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900/50 sm:text-sm transition-all', 'placeholder': 'You@gmail.com'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'block w-full rounded-lg border border-gray-300 py-3 pl-10 pr-4 placeholder-gray-400 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900/50 sm:text-sm transition-all', 'placeholder': '••••••••'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'block w-full rounded-lg border border-gray-300 py-3 pl-10 pr-4 placeholder-gray-400 shadow-sm focus:border-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-900/50 sm:text-sm transition-all', 'placeholder': '••••••••'}))
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')