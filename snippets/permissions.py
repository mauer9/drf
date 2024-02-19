from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only snippet owner can POST, PUT, PATCH, DELETE it.
    """

    message = "You are not the owner of this snippet. You can not edit or delete it"

    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # POST, PUT, PATCH, DELETE
        return request.user == obj.owner
