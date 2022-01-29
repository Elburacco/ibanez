from django.contrib import admin
from .models import Visitor
from django.contrib.admin.options import get_permission_codename
from django.core.exceptions import PermissionDenied

# # Register your models here.
@admin.register(Visitor)
class AccountWithIBANAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'iban']
    # readonly_fields = ['owner',]

    def has_change_permission(self, request, obj=Visitor):
        """
        Return True if the given request has permission to change the given
        Django model instance, the default implementation doesn't examine the
        `obj` parameter.

        Can be overridden by the user in subclasses. In such case it should
        return True if the given request has permission to change the `obj`
        model instance. If `obj` is None, this should return True if the given
        request has permission to change *any* object of the given type.
        """
        opts = self.opts
        codename = get_permission_codename('change', opts)
        if obj:
            if obj.owner == request.user:
                return request.user.has_perm("%s.%s" % (opts.app_label, codename))
        return False

    # def has_delete_permission(self, request, obj=Visitor):
    #     if self.opts.auto_created:
    #         # Same comment as has_add_permission().
    #         # if obj:
    #         print(obj.owner)
    #         # if obj.owner == request.user:
    #
    #         return self._has_any_perms_for_target_model(request, ['change'])
    #     return super().has_delete_permission(request, obj)
    #     # return False





    # def delete_model(self, request, obj):
    #     if obj.owner == request.user:
    #         obj.delete()
    #     return
    # #
    # def update_model(self, request, obj):
    #     if obj.owner == request.user:
    #         obj.delete()
    #     return


