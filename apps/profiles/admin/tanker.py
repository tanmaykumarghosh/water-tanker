from django.contrib import admin

from ..models import Tanker


@admin.register(Tanker)
class TankerAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "plate_number",
        "driver",
        "capacity",
        "service_type",
        "status",
        "is_active",
    )

    search_fields = (
        "plate_number",
        "registration_number",
        "driver__user__phone",
    )

    list_filter = (
        "status",
        "service_type",
        "capacity",
        "is_active",
    )

    autocomplete_fields = (
        "driver",
        "capacity",
    )