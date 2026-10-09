from django.contrib import admin

from ..models import RequestAllocation


@admin.register(RequestAllocation)
class RequestAllocationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "service_request",
        "driver",
        "tanker",
        "allocated_tankers",
        "allocated_capacity",
        "allocation_status",
        "accepted_at",
    )

    list_filter = (
        "allocation_status",
    )

    search_fields = (
        "service_request__request_number",
        "driver__user__phone",
        "tanker__plate_number",
    )

    autocomplete_fields = (
        "service_request",
        "quotation",
        "driver",
        "tanker",
        "allocated_capacity",
    )

    readonly_fields = (
        "uuid",
        "created_at",
        "updated_at",
    )