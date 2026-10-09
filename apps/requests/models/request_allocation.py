import uuid

from django.db import models

from apps.common.models import Capacity
from apps.profiles.models import DriverProfile, Tanker
from apps.requests.models.quotation import Quotation
from apps.requests.models.service_request import ServiceRequest
from ..enums import AllocationStatus

class RequestAllocation(models.Model):

  
    id = models.BigAutoField(primary_key=True)

    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    service_request = models.ForeignKey(
        ServiceRequest,
        on_delete=models.CASCADE,
        db_column="service_request_id",
        related_name="allocations",
    )

    # quotation = models.ForeignKey(
    #     Quotation,
    #     on_delete=models.CASCADE,
    #     db_column="quotation_id",
    #     related_name="allocations",
    # )
    quotation = models.ForeignKey(
        Quotation,
        on_delete=models.CASCADE,
        db_column="quotation_id",
        related_name="allocations",
        null=True,
        blank=True,
    )

    driver = models.ForeignKey(
        DriverProfile,
        on_delete=models.CASCADE,
        db_column="driver_id",
        related_name="allocations",
    )

    tanker = models.ForeignKey(
        Tanker,
        on_delete=models.CASCADE,
        db_column="tanker_id",
        related_name="allocations",
    )

    allocated_tankers = models.PositiveIntegerField(default=1)

    allocated_capacity = models.ForeignKey(
        Capacity,
        on_delete=models.PROTECT,
        db_column="allocated_capacity_id",
        related_name="allocations",
    )

    accepted_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    departed_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    delivery_started_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    completed_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    cancelled_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    allocation_status = models.CharField(
        max_length=20,
        choices=AllocationStatus.choices,
        default=AllocationStatus.PENDING,
    )

    admin_notes = models.TextField(
        blank=True,
        null=True,
    )

    driver_notes = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    arrived_at = models.DateTimeField(
        null=True,
        blank=True,
    )


    class Meta:
        db_table = "request_allocations"
        managed = False
        ordering = ["-created_at"]

    def __str__(self):
        return f"Allocation #{self.id} - {self.service_request.request_number}"