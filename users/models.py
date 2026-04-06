from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='users_images/', null=True, blank=True)
    isSaler = models.BooleanField(default=False)
    storeName = models.CharField(max_length=100, null=False)
