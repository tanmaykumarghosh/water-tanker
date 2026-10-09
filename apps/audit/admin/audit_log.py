from django.contrib import admin

from ..models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "action",
        "table_name",
        "record_id",
        "created_at",
    )

    list_filter = (
        "action",
        "table_name",
    )

    search_fields = (
        "action",
        "table_name",
        "user__phone",
    )

    autocomplete_fields = (
        "user",
    )

    readonly_fields = (
        "created_at",
        "old_values",
        "new_values",
    )

    ordering = (
        "-created_at",
    )