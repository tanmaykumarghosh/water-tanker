from django.contrib import admin

from ..models import ProviderProfile
from ..forms import ProviderProfileAdminForm

@admin.register(ProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    form = ProviderProfileAdminForm

    fieldsets = (
        (
            "Account Information",
            {
                "fields": (
                    "first_name",
                    "middle_name",
                    "last_name",
                    "phone",
                    "email",
                    "password",
                )
            },
        ),
        (
            "Profile Information",
            {
                "fields": (
                    "company_name",
                    "business_registration",
                    "tax_number",
                    "business_address",
                    "business_location",
                    "rating",
                    "total_contracts",
                )
            },
        ),
    )


    list_display = (
        "id",
        "company_name",
        "user",
        "rating",
        "total_contracts",
    )

    search_fields = (
        "company_name",
        "business_registration",
        "tax_number",
    )

    autocomplete_fields = (
        "user",
    )

    list_per_page = 25