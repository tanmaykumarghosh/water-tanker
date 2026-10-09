from django.contrib import admin

from ..models import RequestEvent


@admin.register(RequestEvent)
class RequestEventAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "service_request",
        "event_type",
        "user",
        "created_at",
    )

    list_filter = (
        "event_type",
    )

    search_fields = (
        "service_request__request_number",
        "title",
    )

    autocomplete_fields = (
        "service_request",
        "allocation",
        "user",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )