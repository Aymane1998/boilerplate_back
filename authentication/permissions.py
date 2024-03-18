from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return (
            request.user.groups.filter(name="ADMIN").exists()
            or request.user.is_staff
            or request.user.is_superuser
        )
