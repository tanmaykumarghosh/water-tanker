from rest_framework import serializers

from apps.requests.api.serializers.create_request import (
    CreateRequestSerializer,
)


class CreatePublicRequestSerializer(CreateRequestSerializer):
    """
    Public serializer used by customers without login.
    Extends the existing CreateRequestSerializer.
    """

    first_name = serializers.CharField(
        max_length=100,
    )

    phone = serializers.CharField(
        max_length=20,
    )

    def validate_phone(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Phone number is required."
            )

        return value