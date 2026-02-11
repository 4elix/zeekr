from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='images/products/model')
    power_reserve = models.CharField(max_length=144, null=True, blank=True, verbose_name='Запас хода')
    overclocking = models.CharField(max_length=144, null=True, blank=True, verbose_name='Разгон')
    charging_time = models.CharField(max_length=144, null=True, blank=True, verbose_name='Время зарядки')
    ground_clearance = models.CharField(max_length=144, null=True, blank=True, verbose_name='Дорожный просвет')
    charging_speeds = models.CharField(max_length=144, null=True, blank=True, verbose_name='Скорость зарядки')
    hybrid_motor = models.CharField(max_length=144, null=True, blank=True, verbose_name='Гибридный мотор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class BodyColor(models.Model):
    name_color_user = models.CharField(max_length=155)
    name_color = models.CharField(max_length=155)
    hex = models.CharField(max_length=12)
    image_preview = models.ImageField(upload_to='images/products/body_color')
    product = models.ForeignKey(Products, on_delete=models.PROTECT, related_name='body_color_info')

    def __str__(self):
        return self.name_color_user


class InteriorColor(models.Model):
    name_color_user = models.CharField(max_length=155)
    name_color = models.CharField(max_length=155)
    hex = models.CharField(max_length=12)
    hex_sub = models.CharField(max_length=12)
    image_preview = models.ImageField(upload_to='images/products/interior_color')
    product = models.ForeignKey(Products, on_delete=models.PROTECT, related_name='interior_color_info')

    def __str__(self):
        return self.name_color_user


class ExteriorFeatures(models.Model):
    image = models.ImageField(upload_to='images/products/exterior_features')
    description = models.TextField()
    product = models.ForeignKey(Products, on_delete=models.PROTECT, related_name='exterior_features_info')


class InteriorFeatures(models.Model):
    image = models.ImageField(upload_to='images/products/interior_features')
    description = models.TextField()
    product = models.ForeignKey(Products, on_delete=models.PROTECT, related_name='interior_features_info')


class TestDrive(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    name_customer = models.CharField(max_length=255)
    phone_number_customer = models.CharField(max_length=13)

    def __str__(self):
        return self.name_customer


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_id = models.BigIntegerField(unique=True)

