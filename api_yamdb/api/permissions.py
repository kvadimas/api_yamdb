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


class IsAdminSuperuserOrReadOnly(permissions.BasePermission):
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


class IsAuthorAdminModeratorOrReadOnly(permissions.BasePermission):
    aam_methods = ('PUT', 'PATCH', 'DELETE')

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj,):
        if request.method in IsAuthorAdminModeratorOrReadOnly.aam_methods:
            return (
                request.user.is_authenticated and (
                    obj.author == request.user
                    or request.user.is_admin
                    or request.user.is_staff
                    or request.user.is_moderator
                )
            )
        else:
            return (request.method in permissions.SAFE_METHODS
                    or request.user.is_authenticated)
