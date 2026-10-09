from django.contrib import admin

from ..models import DeliveryOTP


@admin.register(DeliveryOTP)
class DeliveryOTPAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "allocation",
        "otp",
        "otp_status",
        "expires_at",
        "verified_at",
        "created_at",
    )

    list_filter = (
        "otp_status",
    )

    search_fields = (
        "allocation__service_request__request_number",
        "otp",
    )

    autocomplete_fields = (
        "allocation",
    )

    readonly_fields = (
        "created_at",
        "verified_at",
    )

    ordering = (
        "-created_at",
    )