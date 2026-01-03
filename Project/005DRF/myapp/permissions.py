from rest_framework import permissions


class isAdminUserOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
    
    