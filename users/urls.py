from django.urls import path

from .views import auth_page, join_page, profile_page, logout_view, reset_password_page

app_name = 'users'

urlpatterns = [
    path('join/', join_page, name='join_page'),
    path('auth/', auth_page, name='auth_page'),
    path('profile/', profile_page, name='profile_page'),
    path('logout/', logout_view, name='logout_view'),
    path('reset/', reset_password_page, name='reset_password_page')
]