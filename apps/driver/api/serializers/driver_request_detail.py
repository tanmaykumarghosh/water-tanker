from rest_framework import serializers

from apps.requests.models import RequestRecipient


class DriverRequestDetailSerializer(serializers.ModelSerializer):

    request_id = serializers.IntegerField(
        source="service_request.id",
        read_only=True,
    )

    request_number = serializers.CharField(
        source="service_request.request_number",
    )

    request_type = serializers.CharField(
        source="service_request.request_type",
    )

    fulfillment_type = serializers.CharField(
        source="service_request.fulfillment_type",
    )

    service_type = serializers.CharField(
        source="service_request.service_type",
    )

    capacity = serializers.CharField(
        source="service_request.capacity.display_name",
    )

    number_of_tankers = serializers.IntegerField(
        source="service_request.number_of_tankers",
    )

    budget_amount = serializers.DecimalField(
        source="service_request.budget_amount",
        max_digits=12,
        decimal_places=2,
    )

    delivery_address = serializers.CharField(
        source="service_request.delivery_address",
    )

    preferred_delivery_datetime = serializers.DateTimeField(
        source="service_request.preferred_delivery_datetime",
    )

    notes = serializers.CharField(
        source="service_request.notes",
    )

    class Meta:

        model = RequestRecipient

        fields = (
            "id",
            "request_id",
            "request_number",
            "request_type",
            "fulfillment_type",
            "service_type",
            "capacity",
            "number_of_tankers",
            "budget_amount",
            "delivery_address",
            "preferred_delivery_datetime",
            "notes",
            "distance_km",
            "response",
            "viewed_at",
            "created_at",
        )