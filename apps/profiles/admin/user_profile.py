from django.contrib import admin

from ..models import UserProfile
from ..forms import UserProfileAdminForm

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    form = UserProfileAdminForm

    fieldsets = (
        (
            "Account Information",
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
            "Profile Information",
            {
                "fields": (
                    "gender",
                    "date_of_birth",
                    "country",
                    "province",
                    "district",
                    "address",
                    "location",
                    "profile_photo",
                    "preferred_language",
                )
            },
        ),
    )

    list_display = (
        "id",
        "first_name",
        "user",
        "country",
        "province",
        "district",
    )

    search_fields = (
        "first_name",
        "user__phone",
        "user__email",
    )

    list_filter = (
        "country",
        "province",
        "district",
    )
