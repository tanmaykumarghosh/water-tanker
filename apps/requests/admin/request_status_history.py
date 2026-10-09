from django.contrib import admin

from ..models import RequestStatusHistory


@admin.register(RequestStatusHistory)
class RequestStatusHistoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "service_request",
        "status",
        "changed_by_user",
        "created_at",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "service_request__request_number",
    )

    autocomplete_fields = (
        "service_request",
        "changed_by_user",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )