import uuid

from django.contrib.gis.db import models

from apps.accounts.models import User
from apps.common.models import Capacity, Country, Province, District
from ..enums import (
    RequestStatus,
    RequestType,
    FulfillmentType,
    ServiceType,
)

# class RequestType(models.TextChoices):
#     INSTANT = "INSTANT", "Instant"
#     CONTRACT = "CONTRACT", "Contract"


# class FulfillmentType(models.TextChoices):
#     SINGLE_DRIVER = "SINGLE_DRIVER", "Single Driver"
#     MULTIPLE_DRIVERS = "MULTIPLE_DRIVERS", "Multiple Driver"


# class ServiceType(models.TextChoices):
#     WATER = "WATER", "Water"
#     SEPTIC = "SEPTIC", "Septic"


# class RequestStatus(models.TextChoices):
#     NEW = "NEW", "New"
#     OPEN = "OPEN", "Open"
#     QUOTED = "QUOTED", "Quoted"
#     ASSIGNED = "ASSIGNED", "Assigned"
#     IN_PROGRESS = "IN_PROGRESS", "In Progress"
#     COMPLETED = "COMPLETED", "Completed"
#     CANCELLED = "CANCELLED", "Cancelled"
#     EXPIRED = "EXPIRED", "Expired"


class ServiceRequest(models.Model):

    id = models.BigAutoField(primary_key=True)

    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    request_number = models.CharField(
        max_length=30,
        unique=True,
    )

    requester_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        db_column="requester_user_id",
        related_name="service_requests",
    )

    request_type = models.CharField(
        max_length=20,
        choices=RequestType.choices,
    )

    fulfillment_type = models.CharField(
        max_length=20,
        choices=FulfillmentType.choices,
    )

    service_type = models.CharField(
        max_length=20,
        choices=ServiceType.choices,
    )

    capacity = models.ForeignKey(
        Capacity,
        on_delete=models.PROTECT,
        db_column="capacity_id",
    )

    number_of_tankers = models.PositiveIntegerField(
        default=1,
    )

    budget_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
    )

    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        db_column="country_id",
    )

    province = models.ForeignKey(
        Province,
        on_delete=models.PROTECT,
        db_column="province_id",
    )

    district = models.ForeignKey(
        District,
        on_delete=models.PROTECT,
        db_column="district_id",
        blank=True,
        null=True,
    )

    delivery_address = models.TextField()

    delivery_location = models.PointField(
        geography=True,
        srid=4326,
    )

    preferred_delivery_datetime = models.DateTimeField(
        blank=True,
        null=True,
    )

    notes = models.TextField(
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=RequestStatus.choices,
        default=RequestStatus.NEW,
    )

    expires_at = models.DateTimeField(
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
        managed = False
        db_table = "service_requests"
        ordering = ["-created_at"]

    def __str__(self):
        return self.request_number