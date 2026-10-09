from rest_framework import serializers

from apps.requests.models import DeliveryOTP


class DeliveryOTPSerializer(serializers.ModelSerializer):
    """
    Read serializer.
    """

    class Meta:
        model = DeliveryOTP

        fields = (
            "id",
            "otp_status",
            "expires_at",
            "verified_at",
            "created_at",
        )


class GenerateOTPSerializer(serializers.Serializer):
    """
    Generate OTP request.

    No request body is required.
    """

    pass


class VerifyOTPSerializer(serializers.Serializer):
    """
    Verify customer OTP.
    """

    otp = serializers.CharField(
        max_length=6,
        min_length=6,
        trim_whitespace=True,
    )

    def validate_otp(self, value):

        if not value.isdigit():
            raise serializers.ValidationError(
                "OTP must contain only digits."
            )

        return value