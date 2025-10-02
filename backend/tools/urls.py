from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToolViewSet, UniversityViewSet, MajorViewSet

router = DefaultRouter()
router.register(r'list', ToolViewSet, basename='tool')
router.register(r'universities', UniversityViewSet, basename='university')
router.register(r'majors', MajorViewSet, basename='major')

urlpatterns = [
    path('', include(router.urls)),
]
