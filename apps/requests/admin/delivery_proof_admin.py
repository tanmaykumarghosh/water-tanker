from django.contrib import admin

from ..models import DeliveryProof


@admin.register(DeliveryProof)
class DeliveryProofAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "allocation",
        "uploaded_by",
        "created_at",
    )

    autocomplete_fields = (
        "allocation",
        "uploaded_by",
    )

    search_fields = (
        "allocation__service_request__request_number",
        "uploaded_by__phone",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )