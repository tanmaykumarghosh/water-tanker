from apps.requests.models import RequestRecipient
from apps.requests.enums import RecipientResponse
from django.shortcuts import get_object_or_404

from django.db import transaction
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from apps.profiles.models import (
    DriverProfile,
    Tanker,
)

from apps.requests.models import (
    RequestRecipient,
    RequestAllocation,
    RequestEvent,
)

from apps.requests.enums import (
    RecipientResponse,
    AllocationStatus,
    RequestStatus,
    RequestEventType,
)
import logging

logger = logging.getLogger(__name__)
class DriverRequestService:

    @staticmethod
    def inbox(user):

        print("Tracking Updated")
        logger.info("Driver accepted request")
        logger.warning("GPS location missing")
        logger.error("Something went wrong")

        return (
            RequestRecipient.objects
            .select_related(
                "service_request",
                "service_request__capacity",
            )
            .filter(
                recipient_user=user,
            )
            .exclude(
                response=RecipientResponse.EXPIRED,
            )
            .order_by("-created_at")
        )
    @staticmethod
    def get_request(recipient_id, user):

        recipient = (
            RequestRecipient.objects
            .select_related(
                "service_request",
                "service_request__capacity",
            )
            .get(
                id=recipient_id,
                recipient_user=user,
            )
        )

        if recipient.response == RecipientResponse.PENDING:

            recipient.response = RecipientResponse.VIEWED

            recipient.viewed_at = timezone.now()

            recipient.save(
                update_fields=[
                    "response",
                    "viewed_at",
                ]
            )

        return recipient
    @staticmethod
    @transaction.atomic
    def accept(recipient_id, tanker_id, user):

        recipient = (
            RequestRecipient.objects
            .select_for_update()
            .select_related(
                "service_request",
            )
            .get(
                id=recipient_id,
                recipient_user=user,
            )
        )

        if recipient.response not in (
            RecipientResponse.PENDING,
            RecipientResponse.VIEWED,
        ):
            raise ValidationError(
                "This request can no longer be accepted."
            )

        driver = DriverProfile.objects.get(
            user=user,
        )

        tanker = (
            Tanker.objects
            .select_related(
                "capacity",
            )
            .get(
                id=tanker_id,
                driver=driver,
                is_active=True,
            )
        )

        if tanker.status != Tanker.TankerStatus.AVAILABLE:
            raise ValidationError(
                "Selected tanker is not available."
            )

        service_request = recipient.service_request

        if tanker.capacity_id != service_request.capacity_id:
            raise ValidationError(
                "Selected tanker capacity does not match the request."
            )

        allocation = RequestAllocation.objects.create(
            service_request=service_request,
            quotation=None,
            driver=driver,
            tanker=tanker,
            allocated_tankers=1,
            allocated_capacity=tanker.capacity,
            allocation_status=AllocationStatus.ACCEPTED,
            accepted_at=timezone.now(),
        )

        recipient.response = RecipientResponse.ACCEPTED
        recipient.responded_at = timezone.now()

        recipient.save(
            update_fields=[
                "response",
                "responded_at",
            ]
        )

        service_request.status = RequestStatus.ASSIGNED

        service_request.save(
            update_fields=[
                "status",
            ]
        )

        tanker.status = Tanker.TankerStatus.BUSY

        tanker.save(
            update_fields=[
                "status",
            ]
        )

        RequestRecipient.objects.filter(
            service_request=service_request,
            response__in=[
                RecipientResponse.PENDING,
                RecipientResponse.VIEWED,
            ],
        ).exclude(
            id=recipient.id,
        ).update(
            response=RecipientResponse.EXPIRED,
            responded_at=timezone.now(),
        )

        RequestEvent.objects.create(
            service_request=service_request,
            allocation=allocation,
            user=user,
            event_type=RequestEventType.DRIVER_ACCEPTED,
            title="Driver Accepted",
            description="Driver accepted this delivery request.",
            event_data={
                "driver_id": driver.id,
                "tanker_id": tanker.id,
                "allocation_id": allocation.id,
            },
        )

        return allocation
    
    @staticmethod
    @transaction.atomic
    def reject(recipient_id, user):

        recipient = (
            RequestRecipient.objects
            .select_for_update()
            .select_related("service_request")
            .get(
                id=recipient_id,
                recipient_user=user,
            )
        )

        if recipient.response not in (
            RecipientResponse.PENDING,
            RecipientResponse.VIEWED,
        ):
            raise ValidationError(
                "This request can no longer be rejected."
            )

        recipient.response = RecipientResponse.REJECTED
        recipient.responded_at = timezone.now()

        recipient.save(
            update_fields=[
                "response",
                "responded_at",
            ]
        )

        RequestEvent.objects.create(
            service_request=recipient.service_request,
            user=user,
            event_type=RequestEventType.DRIVER_REJECTED,
            title="Driver Rejected",
            description="Driver rejected this request.",
            event_data={
                "recipient_id": recipient.id,
            },
        )

        return recipient