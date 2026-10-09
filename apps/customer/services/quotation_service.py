from django.db import transaction
from django.utils import timezone

from apps.requests.enums import (
    AllocationStatus,
    QuotationStatus,
    RequestStatus,
)

from apps.requests.models import (
    Quotation,
    RequestAllocation,
)

from apps.requests.enums import TankerStatus


class CustomerQuotationService:

    @staticmethod
    def list(request_id, customer):

        return (
            Quotation.objects
            .select_related(
                "service_request",
                "submitted_by_user__user_profile",
                "tanker",
                "tanker__driver",
                "tanker__capacity",
            )
            .filter(
                service_request_id=request_id,
                service_request__requester_user=customer,
            )
            .order_by(
                "quoted_price",
            )
        )
    @staticmethod
    @transaction.atomic
    def accept(
        quotation_id,
        customer,
    ):

        quotation = (
            Quotation.objects
            .select_related(
                "service_request",
                "tanker",
                "tanker__driver",
            )
            .get(
                id=quotation_id,
                service_request__requester_user=customer,
            )
        )

        request = quotation.service_request

        quotation.quotation_status = QuotationStatus.ACCEPTED
        quotation.accepted_at = timezone.now()

        quotation.save(
            update_fields=[
                "quotation_status",
                "accepted_at",
            ]
        )

        (
            Quotation.objects
            .filter(
                service_request=request,
            )
            .exclude(
                id=quotation.id,
            )
            .update(
                quotation_status=QuotationStatus.REJECTED,
                rejected_at=timezone.now(),
            )
        )

        allocation = RequestAllocation.objects.create(
            service_request=request,
            quotation=quotation,
            driver=quotation.tanker.driver,
            tanker=quotation.tanker,
            allocated_tankers=1,
            allocated_capacity=quotation.tanker.capacity,
            allocation_status=AllocationStatus.PENDING,
        )

        request.status = RequestStatus.ALLOCATED

        request.save(
            update_fields=[
                "status",
            ]
        )

        quotation.tanker.status = TankerStatus.BUSY

        quotation.tanker.save(
            update_fields=[
                "status",
            ]
        )

        return allocation