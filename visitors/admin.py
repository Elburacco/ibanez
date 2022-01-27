from django.contrib import admin
from .models import Visitor

# # Register your models here.
@admin.register(Visitor)
class AccountWithIBANAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'iban']


