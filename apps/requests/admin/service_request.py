from django.contrib import admin

from ..models import ServiceRequest


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):

    list_display = (
        "request_number",
        "requester_user",
        "request_type",
        "fulfillment_type",
        "service_type",
        "status",
        "preferred_delivery_datetime",
        "created_at",
    )

    list_filter = (
        "request_type",
        "fulfillment_type",
        "service_type",
        "status",
    )

    search_fields = (
        "request_number",
        "requester_user__phone",
    )

    autocomplete_fields = (
        "requester_user",
        "capacity",
        "country",
        "province",
        "district",
    )

    readonly_fields = (
        "uuid",
        "created_at",
        "updated_at",
    )

    list_per_page = 25