from rest_framework import permissions


class IsAuthorOrModeratorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return (
                obj.author == request.user
                or request.user.is_moderator
            )
        return False