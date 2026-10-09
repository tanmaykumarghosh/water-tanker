from rest_framework import serializers

from apps.requests.models import RequestRecipient


class DriverRequestListSerializer(serializers.ModelSerializer):

    request_id = serializers.IntegerField(
        source="service_request.id",
        read_only=True,
    )

    request_number = serializers.CharField(
        source="service_request.request_number",
        read_only=True,
    )

    service_type = serializers.CharField(
        source="service_request.service_type",
        read_only=True,
    )

    capacity = serializers.CharField(
        source="service_request.capacity.display_name",
        read_only=True,
    )

    delivery_address = serializers.CharField(
        source="service_request.delivery_address",
        read_only=True,
    )

    preferred_delivery_datetime = serializers.DateTimeField(
        source="service_request.preferred_delivery_datetime",
        read_only=True,
    )

    class Meta:
        model = RequestRecipient

        fields = (
            "id",
            "request_id",
            "request_number",
            "service_type",
            "capacity",
            "delivery_address",
            "preferred_delivery_datetime",
            "distance_km",
            "response",
            "created_at",
        )