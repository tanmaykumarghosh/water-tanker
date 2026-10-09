from rest_framework import serializers

from apps.requests.models import DeliveryTracking


class TrackingSerializer(serializers.ModelSerializer):
    """
    Read serializer.
    """

    class Meta:
        model = DeliveryTracking

        fields = (
            "id",
            "latitude",
            "longitude",
            "accuracy",
            "speed",
            "heading",
            "tracking_status",
            "tracked_at",
        )


class UpdateLocationSerializer(serializers.Serializer):
    """
    Driver GPS update serializer.
    """

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


class ArrivedSerializer(UpdateLocationSerializer):
    """
    Driver arrived at destination.
    """

    pass


class DeliveryStartSerializer(UpdateLocationSerializer):
    """
    Driver started unloading.
    """

    pass


class DepartSerializer(UpdateLocationSerializer):
    """
    Driver departed from filling station.
    """

    pass