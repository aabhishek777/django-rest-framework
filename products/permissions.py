

from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):

    def has_permission(self, request, view):
        print(request.user.is_staff)
        if request.user.is_staff:
            return True
        return super().has_permission(request, view)

    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user)
    #     if user.is_staff:
    #         if user.has_perm('products.view_products'): # app_name.action(view, delete, edit,)_model_name
    #             return True
    #     return False
