from django.contrib import admin

from ..models import Capacity

@admin.register(Capacity)
class CapacityAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "display_name",
        "liters",
        "is_active",
    )

    search_fields = (
        "display_name",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "liters",
    )

    readonly_fields = (
        "created_at",
    )