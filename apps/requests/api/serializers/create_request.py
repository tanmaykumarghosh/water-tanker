from django.contrib.gis.geos import Point
from rest_framework import serializers

from apps.common.models import Country, Province, District, Capacity
from apps.requests.enums import (
    FulfillmentType,
    RequestType,
    ServiceType,
)


class CreateRequestSerializer(serializers.Serializer):
    request_type = serializers.ChoiceField(
        choices=RequestType.choices
    )

    fulfillment_type = serializers.ChoiceField(
        choices=FulfillmentType.choices
    )

    service_type = serializers.ChoiceField(
        choices=ServiceType.choices
    )

    capacity_id = serializers.IntegerField()

    number_of_tankers = serializers.IntegerField(
        min_value=1,
        default=1,
    )

    budget_amount = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        required=False,
        allow_null=True,
    )

    country_id = serializers.IntegerField()

    province_id = serializers.IntegerField()

    district_id = serializers.IntegerField(
        required=False,
        allow_null=True,
    )

    delivery_address = serializers.CharField()

    latitude = serializers.FloatField()

    longitude = serializers.FloatField()

    preferred_delivery_datetime = serializers.DateTimeField(
        required=False,
        allow_null=True,
    )

    notes = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    def validate_capacity_id(self, value):
        if not Capacity.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Invalid capacity.")
        return value

    def validate_country_id(self, value):
        if not Country.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Invalid country.")
        return value

    def validate_province_id(self, value):
        if not Province.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Invalid province.")
        return value

    def validate_district_id(self, value):
        if value is None:
            return value

        if not District.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Invalid district.")

        return value

    def validate(self, attrs):

        latitude = attrs.pop("latitude")
        longitude = attrs.pop("longitude")

        attrs["delivery_location"] = Point(
            longitude,
            latitude,
            srid=4326,
        )

        return attrs