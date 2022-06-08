from rest_framework import permissions
from .permissions import IsStaffEditorPermission, IsOwner


class IsStaffEditorPermissionMixin:
    permission_classes = [permissions.IsAuthenticated, IsStaffEditorPermission]


class IsOwnerPermissionMixin:
    permission_classes = [permissions.DjangoModelPermissions, IsOwner]
