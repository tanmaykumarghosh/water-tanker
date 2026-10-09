from rest_framework import serializers


class LatestRequestSerializer(serializers.Serializer):

    id = serializers.IntegerField()

    response = serializers.CharField()

    created_at = serializers.DateTimeField()

    request_number = serializers.CharField(
        source="service_request.request_number",
    )

    service_type = serializers.CharField(
        source="service_request.service_type",
    )

    budget_amount = serializers.DecimalField(
        source="service_request.budget_amount",
        max_digits=12,
        decimal_places=2,
    )

    capacity = serializers.CharField(
        source="service_request.capacity.name",
    )


class DriverDashboardSerializer(serializers.Serializer):

    available_requests = serializers.IntegerField()

    active_jobs = serializers.IntegerField()

    completed_jobs = serializers.IntegerField()

    latest_requests = LatestRequestSerializer(
        many=True,
    )