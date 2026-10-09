from rest_framework import serializers


class SubmitQuotationSerializer(serializers.Serializer):

    recipient_id = serializers.IntegerField()

    tanker_id = serializers.IntegerField()

    quoted_price = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    estimated_delivery_time = serializers.IntegerField()

    remarks = serializers.CharField(
        required=False,
        allow_blank=True,
    )