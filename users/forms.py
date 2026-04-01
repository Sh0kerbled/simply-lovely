from django.contrib.auth.forms import AuthenticationForm
from users.models import CustomUser

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')