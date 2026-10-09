from rest_framework import serializers

from apps.requests.models import ServiceRequest


class RequestDetailSerializer(serializers.ModelSerializer):

    requester = serializers.CharField(
        source="requester_user.phone",
        read_only=True,
    )

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

    class Meta:

        model = ServiceRequest

        fields = (
            "id",
            "uuid",
            "request_number",
            "requester",
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
            "status",
            "created_at",
        )