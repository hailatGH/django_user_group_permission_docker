from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Permission, Group
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated, IsAdminUser

from .models import CustomUser
from .serializers import UserSerializer, GroupSerializer, PermissionSerializer

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes=[IsAuthenticated, DjangoModelPermissions]
    
    def create(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.add_customuser'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.change_customuser'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        return super().update(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.view_customuser'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.view_customuser'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        return super().list(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.delete_customuser'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        return super().destroy(request, *args, **kwargs)

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    permission_classes=[DjangoModelPermissions, IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.add_group'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.change_group'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        return super().update(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.view_group'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.view_group'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        return super().list(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.delete_group'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        return super().destroy(request, *args, **kwargs)

class PermissionViewSet(ModelViewSet):
    queryset = Permission.objects.all().order_by('id')
    serializer_class = PermissionSerializer
    permission_classes=[DjangoModelPermissions, IsAuthenticated, IsAdminUser]
    
    def create(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.add_permission'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.change_permission'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        return super().update(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.view_permission'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.view_permission'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        return super().list(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        if not request.user.has_perm('accounts.delete_permission'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=403)
        return super().destroy(request, *args, **kwargs)