from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    ordering = ("id",)

    list_display = (
    "id",
    "first_name",
    "last_name",
    "phone",
    "email",
    "role",
    "status",
    "is_staff",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "middle_name",
                    "last_name",
                    "phone",
                    "email",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "role",
                    "status",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "middle_name",
                    "last_name",
                    "phone",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )