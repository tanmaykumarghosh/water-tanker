from rest_framework import serializers

from apps.requests.models import ServiceRequest


class CustomerRequestListSerializer(serializers.ModelSerializer):

    capacity = serializers.CharField(
        source="capacity.display_name",
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
            "delivery_address",
            "status",
            "created_at",
        )