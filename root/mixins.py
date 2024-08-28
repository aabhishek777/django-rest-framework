

from rest_framework import permissions
from products.permissions import IsStaffEditorPermission


class StaffEditorPermissionMixins():
    permissions_class = [permissions.IsAdminUser, IsStaffEditorPermission]
