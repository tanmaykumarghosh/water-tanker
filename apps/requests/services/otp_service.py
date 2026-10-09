import random
from datetime import timedelta

from django.db import transaction
from django.utils import timezone

from apps.requests.enums import OTPStatus
from apps.requests.models import DeliveryOTP, RequestAllocation


class OTPService:

    OTP_LENGTH = 6
    OTP_EXPIRY_MINUTES = 10

    @staticmethod
    def generate_otp():
        """
        Generate a random 6-digit OTP.
        """
        return str(random.randint(100000, 999999))

    @classmethod
    @transaction.atomic
    def create_otp(cls, allocation: RequestAllocation):
        """
        Create a new OTP for an allocation.
        Expire any existing pending OTPs.
        """

        DeliveryOTP.objects.filter(
            allocation=allocation,
            otp_status=OTPStatus.PENDING,
        ).update(
            otp_status=OTPStatus.EXPIRED,
        )

        otp = cls.generate_otp()

        delivery_otp = DeliveryOTP.objects.create(
            allocation=allocation,
            otp=otp,
            expires_at=timezone.now() + timedelta(minutes=cls.OTP_EXPIRY_MINUTES),
        )

        return delivery_otp

    @staticmethod
    def get_active_otp(allocation: RequestAllocation):
        """
        Return the latest active OTP.
        """

        return (
            DeliveryOTP.objects.filter(
                allocation=allocation,
                otp_status=OTPStatus.PENDING,
            )
            .order_by("-created_at")
            .first()
        )

    @classmethod
    @transaction.atomic
    def verify_otp(cls, allocation: RequestAllocation, otp: str):
        """
        Verify customer OTP.
        """

        delivery_otp = cls.get_active_otp(allocation)

        if not delivery_otp:
            return False, "OTP not found."

        if timezone.now() > delivery_otp.expires_at:
            delivery_otp.otp_status = OTPStatus.EXPIRED
            delivery_otp.save(update_fields=["otp_status"])
            return False, "OTP has expired."

        if delivery_otp.otp != otp:
            return False, "Invalid OTP."

        delivery_otp.otp_status = OTPStatus.VERIFIED
        delivery_otp.verified_at = timezone.now()

        delivery_otp.save(
            update_fields=[
                "otp_status",
                "verified_at",
            ]
        )

        return True, delivery_otp

    @classmethod
    def resend_otp(cls, allocation: RequestAllocation):
        """
        Generate a fresh OTP.
        """

        return cls.create_otp(allocation)