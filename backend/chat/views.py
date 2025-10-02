from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, Message
from .serializers import ConversationSerializer, ConversationListSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """
    对话会话视图集
    """
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ConversationListSerializer
        return ConversationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
        """发送消息到对话"""
        conversation = self.get_object()
        content = request.data.get('content', '')

        if not content:
            return Response({'error': '消息内容不能为空'}, status=status.HTTP_400_BAD_REQUEST)

        # 创建用户消息
        user_message = Message.objects.create(
            conversation=conversation,
            role='user',
            content=content
        )

        # TODO: 集成AI服务生成回复
        assistant_response = "这是一个示例回复。请集成您的AI服务。"

        # 创建助手消息
        assistant_message = Message.objects.create(
            conversation=conversation,
            role='assistant',
            content=assistant_response
        )

        return Response({
            'user_message': MessageSerializer(user_message).data,
            'assistant_message': MessageSerializer(assistant_message).data
        })

    @action(detail=True, methods=['delete'])
    def clear_messages(self, request, pk=None):
        """清空对话消息"""
        conversation = self.get_object()
        conversation.messages.all().delete()
        return Response({'message': '对话已清空'})


class MessageViewSet(viewsets.ModelViewSet):
    """
    消息视图集
    """
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Message.objects.filter(conversation__user=self.request.user)
