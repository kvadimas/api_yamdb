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


class IsAdminSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (request.user.is_admin or request.user.is_staff)
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated
            and (request.user.is_admin or request.user.is_staff)
        )
