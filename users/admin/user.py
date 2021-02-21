from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models.user import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ("Главная информация", {"fields": ("email", "password")}),
        ("Личная информация", {"fields": ("username", "first_name", "last_name")}),
        ("Статус", {"fields": ("is_staff", "is_superuser", "is_active")}),
    )
