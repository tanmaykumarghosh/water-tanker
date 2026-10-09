import uuid

from django.db import models

from apps.accounts.models import User
from apps.requests.models.service_request import ServiceRequest

from apps.profiles.models import Tanker


class Quotation(models.Model):

    class QuotationStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ACCEPTED = "ACCEPTED", "Accepted"
        REJECTED = "REJECTED", "Rejected"
        CANCELLED = "CANCELLED", "Cancelled"

    id = models.BigAutoField(primary_key=True)

    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    service_request = models.ForeignKey(
        ServiceRequest,
        on_delete=models.CASCADE,
        related_name="quotations",
    )

    submitted_by_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="quotations",
    )

    tanker = models.ForeignKey(
        Tanker,
        on_delete=models.CASCADE,
        db_column="tanker_id",
        related_name="quotations",
    )

    quoted_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    estimated_delivery_time = models.IntegerField(
        blank=True,
        null=True,
        help_text="Estimated delivery time in minutes",
    )

    remarks = models.TextField(
        blank=True,
        null=True,
    )

    quotation_status = models.CharField(
        max_length=20,
        choices=QuotationStatus.choices,
        default=QuotationStatus.PENDING,
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True,
    )

    accepted_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    rejected_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        db_table = "quotations"
        managed = False
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.service_request.request_number} - "
            f"{self.submitted_by_user.phone}"
        )