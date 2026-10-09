from rest_framework import serializers


class DriverTrackingSerializer(serializers.Serializer):

    latitude = serializers.DecimalField(
        max_digits=25,
        decimal_places=7,
    )

    longitude = serializers.DecimalField(
        max_digits=25,
        decimal_places=7,
    )

    accuracy = serializers.DecimalField(
        max_digits=25,
        decimal_places=7,
        required=False,
        allow_null=True,
    )

    speed = serializers.DecimalField(
        max_digits=25,
        decimal_places=7,
        required=False,
        allow_null=True,
    )

    heading = serializers.DecimalField(
        max_digits=25,
        decimal_places=7,
        required=False,
        allow_null=True,
    )