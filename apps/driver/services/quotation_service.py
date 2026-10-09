from django.db import transaction
from django.utils import timezone

from apps.profiles.models import DriverProfile, Tanker
from apps.requests.models import (
    Quotation,
    RequestRecipient,
)


class DriverQuotationService:

    @staticmethod
    @transaction.atomic
    def submit(user, data):

        recipient = (
            RequestRecipient.objects
            .select_related(
                "service_request",
            )
            .get(
                id=data["recipient_id"],
                recipient_user=user,
            )
        )

        driver = DriverProfile.objects.get(
            user=user
        )

        tanker = Tanker.objects.get(
            id=data["tanker_id"],
            driver=driver,
        )

        service_request = recipient.service_request

        if tanker.capacity_id != service_request.capacity_id:
            raise ValueError("Capacity mismatch.")

        if tanker.service_type != service_request.service_type:
            raise ValueError("Service type mismatch.")

        quotation = Quotation.objects.create(
            service_request=service_request,
            submitted_by_user=user,
            tanker=tanker,
            quoted_price=data["quoted_price"],
            estimated_delivery_time=data[
                "estimated_delivery_time"
            ],
            remarks=data.get("remarks"),
            submitted_at=timezone.now(),
        )

        return quotation
    
    @staticmethod
    def my_quotations(user):

        return (
            Quotation.objects
            .select_related(
                "service_request",
                "service_request__capacity",
                "tanker",
            )
            .filter(
                submitted_by_user=user,
            )
            .order_by("-submitted_at")
        )