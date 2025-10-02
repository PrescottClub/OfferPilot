import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.conf import settings
from users.models import User
from users.serializers import UserDetailSerializer


class WeChatLoginView(APIView):
    """
    微信小程序登录接口
    """
    permission_classes = [AllowAny]

    def post(self, request):
        code = request.data.get('code')

        if not code:
            return Response({'error': '缺少code参数'}, status=status.HTTP_400_BAD_REQUEST)

        # 调用微信接口获取session_key和openid
        url = 'https://api.weixin.qq.com/sns/jscode2session'
        params = {
            'appid': settings.WECHAT_APP_ID,
            'secret': settings.WECHAT_APP_SECRET,
            'js_code': code,
            'grant_type': 'authorization_code'
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            data = response.json()

            if 'errcode' in data and data['errcode'] != 0:
                return Response({
                    'error': '微信登录失败',
                    'detail': data.get('errmsg', '')
                }, status=status.HTTP_400_BAD_REQUEST)

            openid = data.get('openid')
            session_key = data.get('session_key')
            unionid = data.get('unionid')

            # 查找或创建用户
            user, created = User.objects.get_or_create(
                wechat_openid=openid,
                defaults={
                    'username': openid,
                    'wechat_unionid': unionid,
                }
            )

            # TODO: 生成自定义token或使用Django session
            # 这里简单返回用户信息
            serializer = UserDetailSerializer(user)

            return Response({
                'user': serializer.data,
                'session_key': session_key,
                'is_new_user': created
            })

        except requests.RequestException as e:
            return Response({
                'error': '网络请求失败',
                'detail': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WeChatUserInfoView(APIView):
    """
    更新微信用户信息
    """
    permission_classes = [AllowAny]

    def post(self, request):
        openid = request.data.get('openid')
        nickname = request.data.get('nickname')
        avatar = request.data.get('avatar')

        if not openid:
            return Response({'error': '缺少openid参数'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(wechat_openid=openid)

            if nickname:
                user.nickname = nickname
            # TODO: 处理头像URL或文件上传

            user.save()

            serializer = UserDetailSerializer(user)
            return Response(serializer.data)

        except User.DoesNotExist:
            return Response({'error': '用户不存在'}, status=status.HTTP_404_NOT_FOUND)
