from rest_framework import permissions


class IsAdminSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (request.user.is_admin or request.user.is_staff)
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_admin or request.user.is_staff
        )


class IsAdminOrRO(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated
                and (request.user.is_admin
                     or request.user.is_staff)
                )
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_admin or request.user.is_staff
        )


class IsAuthorOrRO(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return (request.user.is_authenticated
                    and obj.author == request.user)
        else:
            return request.user.is_authenticated


class IsModeratorOrRO(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return (request.user.is_authenticated
                    and request.user.is_moderator)
        else:
            return request.user.is_authenticated
