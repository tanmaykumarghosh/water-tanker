from rest_framework import serializers

from apps.requests.models import RequestAllocation


class AllocationListSerializer(serializers.ModelSerializer):
    """
    Used for allocation listing.
    """

    request_number = serializers.CharField(
        source="service_request.request_number",
        read_only=True,
    )

    customer_name = serializers.CharField(
        source="service_request.customer.full_name",
        read_only=True,
    )

    driver_name = serializers.CharField(
        source="driver.user.full_name",
        read_only=True,
    )

    tanker_number = serializers.CharField(
        source="tanker.registration_number",
        read_only=True,
    )

    capacity = serializers.CharField(
        source="allocated_capacity.name",
        read_only=True,
    )

    class Meta:
        model = RequestAllocation

        fields = (
            "id",
            "uuid",
            "request_number",
            "customer_name",
            "driver_name",
            "tanker_number",
            "capacity",
            "allocated_tankers",
            "allocation_status",
            "created_at",
        )


class AllocationDetailSerializer(serializers.ModelSerializer):
    """
    Used for allocation details.
    """

    request_number = serializers.CharField(
        source="service_request.request_number",
        read_only=True,
    )

    customer_name = serializers.CharField(
        source="service_request.customer.full_name",
        read_only=True,
    )

    customer_phone = serializers.CharField(
        source="service_request.customer.phone",
        read_only=True,
    )

    driver_name = serializers.CharField(
        source="driver.user.full_name",
        read_only=True,
    )

    driver_phone = serializers.CharField(
        source="driver.user.phone",
        read_only=True,
    )

    tanker_number = serializers.CharField(
        source="tanker.registration_number",
        read_only=True,
    )

    capacity = serializers.CharField(
        source="allocated_capacity.name",
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
            "driver_name",
            "driver_phone",
            "tanker_number",
            "capacity",
            "allocated_tankers",
            "allocation_status",
            "accepted_at",
            "departed_at",
            "delivery_started_at",
            "completed_at",
            "admin_notes",
            "driver_notes",
            "created_at",
            "updated_at",
        )