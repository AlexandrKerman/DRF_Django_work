from django.db import models
from django.contrib.auth.models import AbstractUser

class Cities(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name='Город')

class CustomUser (AbstractUser):
    email = models.EmailField(max_length=50, blank=False, unique=True, verbose_name='Почта')
    phone_number = models.CharField(max_length=11, blank=False, verbose_name='Телефон')
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Город id')
    avatar = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['',]
