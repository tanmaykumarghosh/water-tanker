from rest_framework import serializers
from apps.requests.enums import AllocationStatus
from apps.requests.models import RequestAllocation


class DriverActiveJobSerializer(serializers.Serializer):

    id = serializers.IntegerField()

    request_number = serializers.CharField(
        source="service_request.request_number",
    )

    request_status = serializers.CharField(
        source="service_request.status",
    )

    allocation_status = serializers.CharField()

    customer_name = serializers.CharField(
        source="service_request.requester_user.first_name",
    )

    customer_phone = serializers.CharField(
        source="service_request.requester_user.phone",
    )

    delivery_address = serializers.CharField(
        source="service_request.delivery_address",
    )

    budget_amount = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        source="service_request.budget_amount",
    )

    notes = serializers.CharField(
        source="service_request.notes",
    )

    plate_number = serializers.CharField(
        source="tanker.plate_number",
    )

    tanker_capacity = serializers.CharField(
        source="allocated_capacity.display_name",
    )

class DriverJobStatusSerializer(serializers.Serializer):

    status = serializers.ChoiceField(
        choices=[
            AllocationStatus.ARRIVED,
            AllocationStatus.ON_THE_WAY,
            AllocationStatus.DELIVERY_STARTED,
            AllocationStatus.DELIVERED,
        ]
    )

    latitude = serializers.DecimalField(
        max_digits=10,
        decimal_places=7,
    )

    longitude = serializers.DecimalField(
        max_digits=10,
        decimal_places=7,
    )

    accuracy = serializers.DecimalField(
        max_digits=6,
        decimal_places=2,
        required=False,
        allow_null=True,
    )

    speed = serializers.DecimalField(
        max_digits=6,
        decimal_places=2,
        required=False,
        allow_null=True,
    )

    heading = serializers.DecimalField(
        max_digits=6,
        decimal_places=2,
        required=False,
        allow_null=True,
    )

class DriverJobHistorySerializer(serializers.ModelSerializer):

    request_number = serializers.CharField(
        source="service_request.request_number",
        read_only=True,
    )

    customer_name = serializers.CharField(
        source="service_request.requester_user.first_name",
        read_only=True,
    )

    customer_phone = serializers.CharField(
        source="service_request.requester_user.phone",
        read_only=True,
    )

    delivery_address = serializers.CharField(
        source="service_request.delivery_address",
        read_only=True,
    )

    tanker_capacity = serializers.CharField(
        source="allocated_capacity.name",
        read_only=True,
    )

    plate_number = serializers.CharField(
        source="tanker.plate_number",
        read_only=True,
    )

    budget_amount = serializers.DecimalField(
        source="service_request.budget_amount",
        max_digits=12,
        decimal_places=2,
        read_only=True,
    )

    class Meta:

        model = RequestAllocation

        fields = (
            "id",
            "uuid",
            "request_number",
            "customer_name",
            "customer_phone",
            "delivery_address",
            "plate_number",
            "tanker_capacity",
            "budget_amount",
            "allocation_status",
            "accepted_at",
            "arrived_at",
            "departed_at",
            "delivery_started_at",
            "completed_at",
        )
class DriverJobDetailSerializer(serializers.ModelSerializer):

    request_number = serializers.CharField(
        source="service_request.request_number"
    )

    customer_name = serializers.CharField(
        source="service_request.requester_user.first_name"
    )

    customer_phone = serializers.CharField(
        source="service_request.requester_user.phone"
    )

    delivery_address = serializers.CharField(
        source="service_request.delivery_address"
    )

    notes = serializers.CharField(
        source="service_request.notes"
    )

    plate_number = serializers.CharField(
        source="tanker.plate_number"
    )

    tanker_capacity = serializers.CharField(
        source="allocated_capacity.display_name"
    )

    class Meta:

        model = RequestAllocation

        fields = "__all__"