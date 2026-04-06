from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import auth_page, join_page, profile_page, logout_view, profile_edit, saler_register

app_name = 'users'

urlpatterns = [
    path('join/', join_page, name='join_page'),
    path('auth/', auth_page, name='auth_page'),
    path('profile/', profile_page, name='profile_page'),
    path('logout/', logout_view, name='logout_view'),
    path('password-reset/', PasswordResetView.as_view(template_name='password_reset_form.html', email_template_name='password_reset_email.html' ,success_url=reverse_lazy('users:password_reset_done')), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', success_url=reverse_lazy('users:password_reset_complete')), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('saler-register/', saler_register, name='saler_register')
]