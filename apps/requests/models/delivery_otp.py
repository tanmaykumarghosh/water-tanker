from django.db import models

from apps.requests.models.request_allocation import RequestAllocation
from ..enums import OTPStatus


class DeliveryOTP(models.Model):

    id = models.BigAutoField(primary_key=True)

    allocation = models.OneToOneField(
        RequestAllocation,
        on_delete=models.CASCADE,
        db_column="allocation_id",
        related_name="delivery_otp",
    )

    otp = models.CharField(
        max_length=6,
    )

    otp_status = models.CharField(
        max_length=20,
        choices=OTPStatus.choices,
        default=OTPStatus.PENDING,
    )

    verified_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    expires_at = models.DateTimeField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "delivery_otps"
        managed = False
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.allocation_id} - {self.otp_status}"