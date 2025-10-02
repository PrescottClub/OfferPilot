from django.urls import path
from .views import WeChatLoginView, WeChatUserInfoView

urlpatterns = [
    path('login/', WeChatLoginView.as_view(), name='wechat-login'),
    path('userinfo/', WeChatUserInfoView.as_view(), name='wechat-userinfo'),
]
