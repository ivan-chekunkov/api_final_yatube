from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return True if (request.method in permissions.SAFE_METHODS
                        or obj.author == request.user) else False
