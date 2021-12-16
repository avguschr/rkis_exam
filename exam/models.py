from django.db import models
from django.contrib.auth.models import AbstractUser

class SomeUser(AbstractUser):
    def __str__(self):
        return self.username
    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'

class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    img = models.ImageField(upload_to='static/img/', null=False)
    description = models.TextField(null=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'

class Order(models.Model):
    owner = models.ForeignKey('SomeUser', on_delete=models.CASCADE, null=False)
    products = models.ManyToManyField(Product, blank=False, null=False)
    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'