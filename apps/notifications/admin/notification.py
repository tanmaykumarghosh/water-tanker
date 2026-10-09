from django.contrib import admin

from ..models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "title",
        "notification_type",
        "notification_status",
        "created_at",
    )

    list_filter = (
        "notification_type",
        "notification_status",
    )

    search_fields = (
        "title",
        "user__phone",
    )

    autocomplete_fields = (
        "user",
    )

    readonly_fields = (
        "created_at",
        "read_at",
    )

    ordering = (
        "-created_at",
    )