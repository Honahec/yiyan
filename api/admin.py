from django.contrib import admin
from .models import Sentence

@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'created_at', 'updated_at')
    list_display_links = ('content', 'author')
    search_fields = ('content', 'author')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')