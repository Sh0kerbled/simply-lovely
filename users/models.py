from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    
    full_name = models.CharField("Полное имя", max_length=255)
    email = models.EmailField("Email address", unique=True)