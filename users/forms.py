from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from app.models import Products, Categories
from django import forms
from django.forms import ModelForm
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

class UserEditForm(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'theme-input w-full pl-10 pr-4 py-2.5 rounded-lg border text-sm transition'
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'theme-input w-full pl-7 pr-4 py-2.5 rounded-lg border text-sm transition'
    }), required=False)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'theme-input w-full pl-7 pr-4 py-2.5 rounded-lg border text-sm transition'
    }))

    password = None
    class Meta:
        model = CustomUser
        fields = ('image', 'username', 'email')
    
class SalerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-900 transition'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-900 transition'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-900 transition'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-900 transition'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-900 transition'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-900 transition'
    }))
    storeName = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-900 transition'
    }))
    isSaler = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'mt-0.5 w-4 h-4 accent-gray-900 cursor-pointer'
    }), required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'storeName', 'isSaler')
    
class AddProduct(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-900 transition bg-white'
    }))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'w-full border border-gray-200 rounded-lg pl-8 pr-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-900 transition'
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'hidden'
    }))

    class Meta:
        model = Products
        fields= ('category', 'title', 'price', 'image')
        widgets = {
            'category': forms.RadioSelect(attrs={
                'class': 'w-full border border-gray-200 rounded-lg pl-8 pr-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-900 transition'
            }),
        }

class sellerGoodsCount(forms.ModelForm):
    class Meta:
        model = Products