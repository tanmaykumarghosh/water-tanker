from rest_framework import serializers

from apps.requests.models import ServiceRequest


class CustomerRequestDetailSerializer(serializers.ModelSerializer):

    capacity = serializers.CharField(
        source="capacity.display_name",
        read_only=True,
    )

    country = serializers.CharField(
        source="country.name",
        read_only=True,
    )

    province = serializers.CharField(
        source="province.name",
        read_only=True,
    )

    district = serializers.CharField(
        source="district.name",
        read_only=True,
    )

    quotation_count = serializers.IntegerField(
        read_only=True,
    )

    allocation_count = serializers.IntegerField(
        read_only=True,
    )

    class Meta:

        model = ServiceRequest

        fields = (
            "id",
            "uuid",
            "request_number",
            "request_type",
            "fulfillment_type",
            "service_type",
            "capacity",
            "number_of_tankers",
            "budget_amount",
            "country",
            "province",
            "district",
            "delivery_address",
            "preferred_delivery_datetime",
            "notes",
            "status",
            "quotation_count",
            "allocation_count",
            "created_at",
            "updated_at",
        )