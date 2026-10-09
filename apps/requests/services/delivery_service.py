from django.db import transaction
from django.utils import timezone

from apps.requests.enums import (
    AllocationStatus,
    RequestStatus,
)
from apps.requests.models import (
    DeliveryProof,
    RequestAllocation,
)
from apps.requests.services.otp_service import OTPService
from apps.requests.services.tracking_service import TrackingService


class DeliveryService:

    @staticmethod
    @transaction.atomic
    def complete_delivery(
        *,
        allocation: RequestAllocation,
        otp: str,
        uploaded_by,
        customer_photo=None,
        customer_signature=None,
        remarks=None,
        latitude=None,
        longitude=None,
    ):
        """
        Complete delivery after OTP verification.
        """

        success, result = OTPService.verify_otp(
            allocation=allocation,
            otp=otp,
        )

        if not success:
            return False, result

        proof, _ = DeliveryProof.objects.get_or_create(
            allocation=allocation,
            defaults={
                "uploaded_by": uploaded_by,
            },
        )

        proof.customer_photo = customer_photo
        proof.customer_signature = customer_signature
        proof.remarks = remarks
        proof.uploaded_by = uploaded_by

        proof.save()

        allocation.allocation_status = AllocationStatus.DELIVERED
        allocation.completed_at = timezone.now()

        allocation.save(
            update_fields=[
                "allocation_status",
                "completed_at",
                "updated_at",
            ]
        )

        request = allocation.service_request
        request.status = RequestStatus.COMPLETED
        request.save(update_fields=["status", "updated_at"])

        TrackingService.complete_delivery(
            allocation=allocation,
            latitude=latitude,
            longitude=longitude,
        )

        return True, allocation