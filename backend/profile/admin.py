from django.contrib import admin
from .models import UserProfile, Application


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'undergraduate_school', 'major', 'gpa', 'ielts_score', 'updated_at']
    search_fields = ['user__username', 'user__nickname', 'undergraduate_school', 'major']
    list_filter = ['target_regions', 'graduation_year']
    ordering = ['-updated_at']


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'university_name', 'major_name', 'status', 'application_date', 'deadline']
    list_filter = ['status', 'degree_type', 'application_date']
    search_fields = ['user__username', 'user__nickname', 'university_name', 'major_name']
    ordering = ['-created_at']
