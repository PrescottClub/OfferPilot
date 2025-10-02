from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    自定义用户模型，扩展Django默认用户
    """
    wechat_openid = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name='微信OpenID')
    wechat_unionid = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name='微信UnionID')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='头像')
    nickname = models.CharField(max_length=50, blank=True, verbose_name='昵称')
    phone = models.CharField(max_length=20, blank=True, verbose_name='手机号')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
        db_table = 'users'

    def __str__(self):
        return self.nickname or self.username


class UserAuth(models.Model):
    """
    用户认证信息表
    """
    user_id = models.AutoField(primary_key=True, verbose_name='用户ID')
    user_name = models.CharField(max_length=100, verbose_name='用户名')
    wx_id = models.CharField(max_length=100, verbose_name='微信ID')

    class Meta:
        verbose_name = '用户认证'
        verbose_name_plural = '用户认证'
        db_table = 'user_auth'

    def __str__(self):
        return f"{self.user_name} ({self.wx_id})"
