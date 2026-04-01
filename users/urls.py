from django.urls import path

from .views import auth_page, join_page

app_name = 'users'

urlpatterns = [
    path('join/', join_page, name='join_page'),
    path('auth/', auth_page, name='auth_page')
]