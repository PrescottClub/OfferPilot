from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'nickname', 'avatar', 'phone', 'email', 'created_at']
        read_only_fields = ['id', 'created_at']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'nickname', 'avatar', 'phone', 'email', 'wechat_openid', 'created_at', 'updated_at']
        read_only_fields = ['id', 'wechat_openid', 'created_at', 'updated_at']
