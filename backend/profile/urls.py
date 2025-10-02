from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, ApplicationViewSet

router = DefaultRouter()
router.register(r'info', UserProfileViewSet, basename='userprofile')
router.register(r'applications', ApplicationViewSet, basename='application')

urlpatterns = [
    path('', include(router.urls)),
]
