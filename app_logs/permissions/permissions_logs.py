from rest_framework import permissions
from authentication import enums


class LogsPermission(permissions.BasePermission):
    message = "You don't have access to these informations"

    def isAdmin(self, request):
        return request.user.is_staff

    def has_permission(self, request, view):
        return self.isAdmin(request)

    def has_object_permission(self, request, view, obj):
        return self.isAdmin(request)
