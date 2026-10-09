from rest_framework import serializers


class DriverTankerSerializer(serializers.Serializer):

    id = serializers.IntegerField()

    plate_number = serializers.CharField()

    registration_number = serializers.CharField()

    service_type = serializers.CharField()

    status = serializers.CharField()

    capacity = serializers.CharField(
        source="capacity.display_name",
    )