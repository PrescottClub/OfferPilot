from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Tool, University, Major
from .serializers import (
    ToolSerializer, UniversitySerializer, UniversityDetailSerializer, MajorSerializer
)


class ToolViewSet(viewsets.ReadOnlyModelViewSet):
    """
    工具视图集 - 只读
    """
    queryset = Tool.objects.filter(is_active=True)
    serializer_class = ToolSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']
    filterset_fields = ['category']


class UniversityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    大学视图集 - 只读
    """
    queryset = University.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'name_en', 'city', 'country']
    filterset_fields = ['region', 'country']
    ordering_fields = ['ranking', 'name']
    ordering = ['ranking']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UniversityDetailSerializer
        return UniversitySerializer


class MajorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    专业视图集 - 只读
    """
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'name_en', 'description']
    filterset_fields = ['university', 'degree_type']
