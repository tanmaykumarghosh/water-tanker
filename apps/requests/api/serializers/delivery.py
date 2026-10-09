from rest_framework import serializers

from apps.requests.models import DeliveryProof


class DeliveryProofSerializer(serializers.ModelSerializer):
    """
    Read serializer.
    """

    class Meta:
        model = DeliveryProof

        fields = (
            "id",
            "customer_photo",
            "customer_signature",
            "remarks",
            "created_at",
        )


class CompleteDeliverySerializer(serializers.Serializer):
    """
    Complete delivery request.
    """

    otp = serializers.CharField(
        max_length=6,
        min_length=6,
        trim_whitespace=True,
    )

    customer_photo = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
    )

    customer_signature = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
    )

    remarks = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
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

    def validate_otp(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "OTP must contain only digits."
            )

        return value

    def validate(self, attrs):
        """
        At least one proof should be provided.
        """

        if (
            not attrs.get("customer_photo")
            and not attrs.get("customer_signature")
        ):
            raise serializers.ValidationError(
                "Either customer_photo or customer_signature is required."
            )

        return attrs