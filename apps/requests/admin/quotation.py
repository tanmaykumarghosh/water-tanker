from django.contrib import admin

from ..models import Quotation


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "service_request",
        "submitted_by_user",
        "tanker",
        "quoted_price",
        "quotation_status",
    )

    list_filter = (
        "quotation_status",
    )

    search_fields = (
        "service_request__request_number",
        "submitted_by_user__phone",
    )

    autocomplete_fields = (
        "service_request",
        "submitted_by_user",
        "tanker",
    )

    readonly_fields = (
        "uuid",
        "submitted_at",
        "created_at",
        "updated_at",
    )