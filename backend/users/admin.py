from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'nickname', 'phone', 'email', 'is_staff', 'created_at']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'created_at']
    search_fields = ['username', 'nickname', 'phone', 'email', 'wechat_openid']
    ordering = ['-created_at']

    fieldsets = BaseUserAdmin.fieldsets + (
        ('微信信息', {'fields': ('wechat_openid', 'wechat_unionid')}),
        ('扩展信息', {'fields': ('nickname', 'avatar', 'phone')}),
    )
