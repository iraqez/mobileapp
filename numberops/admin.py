from django.contrib import admin
from .models import ActivationsNum


@admin.register(ActivationsNum)
class ActivationsNumAdmin(admin.ModelAdmin):
    readonly_fields = ['date',]

