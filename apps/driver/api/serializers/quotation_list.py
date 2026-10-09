from rest_framework import serializers

from apps.requests.models import Quotation


class DriverQuotationListSerializer(serializers.ModelSerializer):

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

    tanker = serializers.CharField(
        source="tanker.plate_number",
        read_only=True,
    )

    class Meta:

        model = Quotation

        fields = (
            "id",
            "request_number",
            "service_type",
            "capacity",
            "delivery_address",
            "tanker",
            "quoted_price",
            "estimated_delivery_time",
            "quotation_status",
            "submitted_at",
        )