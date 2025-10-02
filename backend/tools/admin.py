from django.contrib import admin
from .models import Tool, University, Major


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'is_active', 'order', 'created_at']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'description']
    ordering = ['order', '-created_at']


class MajorInline(admin.TabularInline):
    model = Major
    extra = 0
    fields = ['name', 'name_en', 'degree_type', 'duration', 'tuition', 'currency']


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'region', 'country', 'city', 'ranking', 'created_at']
    list_filter = ['region', 'country']
    search_fields = ['name', 'name_en', 'city']
    inlines = [MajorInline]
    ordering = ['ranking']


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ['name', 'university', 'degree_type', 'duration', 'tuition', 'currency']
    list_filter = ['degree_type', 'university__region']
    search_fields = ['name', 'name_en', 'university__name']
    ordering = ['university', 'name']
