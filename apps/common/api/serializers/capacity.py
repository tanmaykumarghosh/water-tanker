from rest_framework import serializers

from apps.common.models import Capacity


class CapacitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Capacity

        fields = (
            "id",
            "liters",
            "display_name",
        )