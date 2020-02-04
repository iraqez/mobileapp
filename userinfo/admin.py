from django.contrib import admin
from .models import OrgInfo, UserInfo


@admin.register(OrgInfo)
class OrgInfoAdmin(admin.ModelAdmin):
    None


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    None