from rest_framework import serializers


class AcceptRequestSerializer(serializers.Serializer):

    tanker_id = serializers.IntegerField()