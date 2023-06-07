from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet, GroupViewSet, PermissionViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]