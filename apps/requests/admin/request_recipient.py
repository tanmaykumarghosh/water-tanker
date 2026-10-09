from django.contrib import admin

from ..models import RequestRecipient


@admin.register(RequestRecipient)
class RequestRecipientAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "service_request",
        "recipient_user",
        "notification_channel",
        "response",
        "distance_km",
        "sent_at",
    )

    list_filter = (
        "notification_channel",
        "response",
    )

    search_fields = (
        "service_request__request_number",
        "recipient_user__phone",
    )

    autocomplete_fields = (
        "service_request",
        "recipient_user",
    )

    ordering = (
        "-id",
    )