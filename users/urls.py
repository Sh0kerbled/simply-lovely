from django.urls import path

from .views import auth_page, join_page, profile_page

app_name = 'users'

urlpatterns = [
    path('join/', join_page, name='join_page'),
    path('auth/', auth_page, name='auth_page'),
    path('profile/', profile_page, name='profile_page')
]