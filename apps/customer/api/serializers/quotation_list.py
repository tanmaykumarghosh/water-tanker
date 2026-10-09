from rest_framework import serializers

from apps.requests.models import Quotation


class CustomerQuotationListSerializer(serializers.ModelSerializer):

    driver_name = serializers.CharField(
        source="submitted_by_user.user_profile.full_name",
        read_only=True,
    )

    driver_rating = serializers.DecimalField(
        source="tanker.driver.rating",
        max_digits=3,
        decimal_places=2,
        read_only=True,
    )

    tanker_plate_number = serializers.CharField(
        source="tanker.plate_number",
        read_only=True,
    )

    capacity = serializers.CharField(
        source="tanker.capacity.display_name",
        read_only=True,
    )

    class Meta:

        model = Quotation

        fields = (
            "id",
            "driver_name",
            "driver_rating",
            "tanker_plate_number",
            "capacity",
            "quoted_price",
            "estimated_delivery_time",
            "remarks",
            "quotation_status",
            "submitted_at",
        )