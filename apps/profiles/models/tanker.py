from django.db import models

from apps.common.models import Capacity
from .driver_profile import DriverProfile


class Tanker(models.Model):

    class ServiceType(models.TextChoices):
        WATER = "WATER", "Water Tanker"
        SEPTIC = "SEPTIC", "Septic Tank Cleaning"

    class TankerStatus(models.TextChoices):
        AVAILABLE = "AVAILABLE", "Available"
        BUSY = "BUSY", "Busy"
        MAINTENANCE = "MAINTENANCE", "Maintenance"
        OFFLINE = "OFFLINE", "Offline"

    id = models.BigAutoField(primary_key=True)

    driver = models.ForeignKey(
        DriverProfile,
        on_delete=models.CASCADE,
        db_column="driver_id",
        related_name="tankers",
    )

    plate_number = models.CharField(
        max_length=50,
        unique=True,
    )

    registration_number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    manufacturer = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    model = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    manufacture_year = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
    )

    capacity = models.ForeignKey(
        Capacity,
        on_delete=models.PROTECT,
        db_column="capacity_id",
        related_name="tankers",
    )

    service_type = models.CharField(
        max_length=20,
        choices=ServiceType.choices,
    )

    status = models.CharField(
        max_length=20,
        choices=TankerStatus.choices,
        default=TankerStatus.AVAILABLE,
    )

    is_active = models.BooleanField(default=True)

    notes = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField()

    updated_at = models.DateTimeField()

    class Meta:
        db_table = "tankers"
        managed = False
        ordering = ["plate_number"]

    def __str__(self):
        return f"{self.plate_number} ({self.capacity})"