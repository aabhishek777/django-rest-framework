

from rest_framework import permissions
from products.permissions import IsStaffEditorPermission
from products.models import Products


class StaffEditorPermissionMixins():
    permissions_class = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserGetQuerySetMixin():
    user_field = 'user'  # TODO we can change the name of the table field

    def get_queryset(self, *args, **kwargs):

        lookup_data = {}
        lookup_data[self.user_field] = self.request.user

        queryset = super().get_queryset(*args, **kwargs)
        return queryset.filter(**lookup_data)
