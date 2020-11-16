from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'updated', 'status')
    list_filter = ('status', 'created', 'publish', 'updated')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
