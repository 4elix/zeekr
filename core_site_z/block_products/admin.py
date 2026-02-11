from django.contrib import admin
from .models import Products, BodyColor, InteriorColor, InteriorFeatures, ExteriorFeatures, TestDrive


class BodyColorInclude(admin.TabularInline):
    model = BodyColor
    extra = 1


class InteriorColorInclude(admin.TabularInline):
    model = InteriorColor
    extra = 1


class InteriorFeaturesInclude(admin.TabularInline):
    model = InteriorFeatures
    extra = 1


class ExteriorFeaturesInclude(admin.TabularInline):
    model = ExteriorFeatures
    extra = 1


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    list_display_links = ['pk', 'title']
    prepopulated_fields = {'slug': ['title']}
    ordering = ['pk']
    inlines = [BodyColorInclude, InteriorColorInclude, InteriorFeaturesInclude, ExteriorFeaturesInclude]


@admin.register(TestDrive)
class TestDriveAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name_customer', 'phone_number_customer']
    list_display_links = ['pk', 'name_customer']
    ordering = ['pk']
    search_fields = ['name_customer', 'phone_number_customer']
