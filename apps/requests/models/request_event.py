import uuid

from django.db import models

from apps.accounts.models import User
from .service_request import ServiceRequest
from .request_allocation import RequestAllocation
from ..enums import RequestEventType


class RequestEvent(models.Model):

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
        related_name="events",
    )

    allocation = models.ForeignKey(
        RequestAllocation,
        on_delete=models.SET_NULL,
        db_column="allocation_id",
        blank=True,
        null=True,
        related_name="events",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        db_column="user_id",
        blank=True,
        null=True,
        related_name="request_events",
    )

    event_type = models.CharField(
        max_length=40,
        choices=RequestEventType.choices,
    )

    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    event_data = models.JSONField(
        blank=True,
        null=True,
    )

    ip_address = models.GenericIPAddressField(
        protocol="both",
        unpack_ipv4=True,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "request_events"
        managed = False
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.service_request.request_number} - {self.event_type}"