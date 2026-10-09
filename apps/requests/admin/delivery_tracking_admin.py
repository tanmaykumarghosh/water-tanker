from django.contrib import admin

from ..models import DeliveryTracking


@admin.register(DeliveryTracking)
class DeliveryTrackingAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "allocation",
        "tracking_status",
        "latitude",
        "longitude",
        "tracked_at",
    )

    list_filter = (
        "tracking_status",
    )

    autocomplete_fields = (
        "allocation",
    )

    ordering = (
        "-tracked_at",
    )

    readonly_fields = (
        "created_at",
    )