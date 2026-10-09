from rest_framework import serializers


class TrackRequestSerializer(serializers.Serializer):

    request_number = serializers.CharField()

    phone = serializers.CharField(max_length=20)