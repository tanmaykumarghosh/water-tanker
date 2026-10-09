from django.db import models

from apps.requests.models.request_allocation import RequestAllocation
from ..enums import TrackingStatus


class DeliveryTracking(models.Model):

    id = models.BigAutoField(primary_key=True)

    allocation = models.ForeignKey(
        RequestAllocation,
        on_delete=models.CASCADE,
        db_column="allocation_id",
        related_name="tracking_logs",
    )

    latitude = models.DecimalField(
        max_digits=25,
        decimal_places=7,
    )

    longitude = models.DecimalField(
        max_digits=25,
        decimal_places=7,
    )

    accuracy = models.DecimalField(
        max_digits=25,
        decimal_places=7,
        blank=True,
        null=True,
    )

    speed = models.DecimalField(
        max_digits=25,
        decimal_places=7,
        blank=True,
        null=True,
    )

    heading = models.DecimalField(
        max_digits=25,
        decimal_places=7,
        blank=True,
        null=True,
    )

    tracking_status = models.CharField(
        max_length=30,
        choices=TrackingStatus.choices,
    )

    tracked_at = models.DateTimeField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "delivery_tracking"
        managed = False
        ordering = ["-tracked_at"]

    def __str__(self):
        return f"{self.allocation_id} @ {self.tracked_at}"