from django.contrib import admin

from .models import News


@admin.register(News)
class NewsRegister(admin.ModelAdmin):
    list_display = ['pk', 'title_news', 'is_active']
    list_display_links = ['pk', 'title_news']
    search_fields = ['title']
    ordering = ['pk']
    prepopulated_fields = {'slug_news': ['title_news']}
