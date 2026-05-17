from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'seller', 'created_at')
    search_fields = ('title', 'author', 'seller__username')
    list_filter = ('created_at',)