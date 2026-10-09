from django.contrib import admin

from ..models import DriverProfile
from ..forms import DriverProfileAdminForm

@admin.register(DriverProfile)
class DriverProfileAdmin(admin.ModelAdmin):

    form = DriverProfileAdminForm

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
                    "national_id",
                    "driving_license",
                    "is_online",
                    "is_available",
                    "current_location",
                    "last_location_update",
                    "rating",
                    "total_completed_jobs",
                )
            },
        ),
    )


    list_display = (
        "id",
        "user__first_name",
        "user",
        "is_online",
        "is_available",
        "rating",
        "total_completed_jobs",
    )

    search_fields = (
        "user__phone",
        "driving_license",
        "national_id",
    )

    list_filter = (
        "is_online",
        "is_available",
    )