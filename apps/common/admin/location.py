from django.contrib import admin
from ..models import Country,Province,District


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "iso_code",
        "is_active",
    )

    search_fields = (
        "name",
        "iso_code",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "country",
        "is_active",
    )

    search_fields = (
        "name",
        "country__name",
    )

    list_filter = (
        "country",
        "is_active",
    )

    list_select_related = (
        "country",
    )

    ordering = (
        "country__name",
        "name",
    )

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "province",
        "country",
        "is_active",
    )

    search_fields = (
        "name",
        "province__name",
        "province__country__name",
    )

    list_filter = (
        "province__country",
        "province",
        "is_active",
    )

    list_select_related = (
        "province",
        "province__country",
    )

    ordering = (
        "province__country__name",
        "province__name",
        "name",
    )

    def country(self, obj):
        return obj.province.country

    country.short_description = "Country"