from django.contrib import admin
from .models import Visitor


# # Register your models here.
@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'iban']
    readonly_fields = ['owner', ]

    def has_change_permission(self, request, obj=None):
        if obj:
            if obj.owner != request.user:
                return False
        if self.opts.auto_created:
            # Same comment as has_add_permission().
            return self._has_any_perms_for_target_model(request, ['change'])
        return super().has_change_permission(request)

    def has_delete_permission(self, request, obj=None):
        if obj:
            print(str(obj.owner), 'obj.owner', request.user, 'request.user')
            print('ni mo')
            if obj.owner != request.user:

                return False
        if self.opts.auto_created:
            # Same comment as has_add_permission().
            return self._has_any_perms_for_target_model(request, ['change'])
        return super().has_delete_permission(request, obj)
